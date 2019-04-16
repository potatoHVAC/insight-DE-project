#!/usr/bin/env python3

import os
import re
import sys
import redis
from time import (time, mktime)
from datetime import datetime
from kafka import KafkaProducer
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

from variable_library import (
    SPARK_MASTER,
    APPNAME,
    KAFKA_BROKERS,
    DATABASE_IP,
    MAIN_KAFKA_TOPIC
)

TOKENS_MAX = 100
BLACKLIST_TIMER = 120
TOKENS_TIMER = 120

def connect_to_redis():
    return redis.Redis(
        host = DATABASE_IP,
        port = 6379
    )
    
def get_ip(raw_log):
    return re.findall('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', raw_log)[0]

def get_time_stamp(raw_log):
    time_stamp_string = re.findall('\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2}', raw_log)[0]
    return datetime.strptime(time_stamp_string, '%d/%b/%Y:%H:%M:%S')

def convert_datetime_to_int(date_time):
    return int(mktime(date_time.timetuple()))

def current_time_stamp():
    return int(time())

def send_logs_to_kafka(input_log, output_log, producer):
    producer.send('olorin_input_logs', input_log.encode('utf-8'))
    producer.flush()
    producer.send('olorin_output_logs', output_log.encode('utf-8'))
    producer.flush()

def format_log_for_visualizer(log):
    return re.sub(' 429 ', ' 200 ', log)

def blacklist_check(ip, red):
    return red.get("blacklist{}".format(ip))

def blacklist_set(ip, time_stamp_sec, red):
    red.set("blacklist{}".format(ip), time_stamp_sec)

def tokens_set(ip, tokens, time_stamp, red):
    redis_value = "{},{}".format(tokens, time_stamp)
    red.set(ip, redis_value, TOKENS_TIMER)

def update_tokens(tokens, last_time_stamp_sec, time_stamp_sec):
    new_token_value = tokens + time_stamp_sec - last_time_stamp_sec - 1
    return max(0, new_token_value)

def check_or_update_ip_token(input_log, red):
    ip = get_ip(input_log)
    time_stamp_sec = convert_datetime_to_int(get_time_stamp(input_log))
    
    if blacklist_check(ip, red):
        blacklist_set(ip, time_stamp_sec, red)
        return format_log_for_visualizer(input_log)

    try:
        tokens, last_time_stamp_sec = [ int(num) for num in red.get(ip).decode('utf-8').split(',') ]
        new_token_value = update_tokens(tokens, last_time_stamp_sec, time_stamp_sec)
        tokens_set(ip, new_token_value, time_stamp_sec, red)

        if new_token_value == 0:
            blacklist_set(ip, time_stamp_sec, red)
            return format_log_for_visualizer(input_log)
        return input_log        
    except:
        tokens_set(ip, TOKENS_MAX // 5, time_stamp_sec, red)
        return input_log        
        
    
def olorin_database_check(line):
    producer = KafkaProducer(bootstrap_servers = KAFKA_BROKERS)
    red = connect_to_redis()
    
    for row in line:
        output_log = check_or_update_ip_token(row[0], red)
        send_logs_to_kafka(row[0], output_log, producer)

def olorin_main(sc, ssc):
    kafkaStreamSaw = KafkaUtils.createDirectStream(
        ssc,
        [MAIN_KAFKA_TOPIC],
        {'metadata.broker.list': KAFKA_BROKERS}
    )
    transactionSaw = kafkaStreamSaw.map(lambda row: row[1].split(','))
    transactionSaw.foreachRDD(lambda rdd: rdd.foreachPartition(olorin_database_check))
    
def main():
    sc = SparkContext(appName = APPNAME)
    sc.setLogLevel("WARN")
    ssc = StreamingContext(sc, 1)

    print(r''' 





                    ________  .__               .__        
                    \_____  \ |  |   __/________|__| ____  
                     /   |   \|  |  /  _ \_  __ \  |/    \ 
                    /    |    \  |_(  <_> )  | \/  |   |  \
                    \_______  /____/\____/|__|  |__|___|  /
                            \/                          \/ 





    ''')

    olorin_main(sc, ssc)
    ssc.start()
    ssc.awaitTermination()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() 
