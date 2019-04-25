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
    MAIN_KAFKA_TOPIC,
    OLORIN_ASCII_LOGO
)

TOKENS_MAX = 100

def connect_to_redis():
    return redis.Redis(
        host = DATABASE_IP,
        port = 6379
    )
    
def get_ip(raw_log):
    return re.findall('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', raw_log)[0]

def get_time_stamp(raw_log):
    '''
    input: string -- raw apache log
    output: datetime
    '''
    time_stamp_string = re.findall('\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2}', raw_log)[0]
    return datetime.strptime(time_stamp_string, '%d/%b/%Y:%H:%M:%S')

def convert_datetime_to_int(date_time):
    return int(mktime(date_time.timetuple()))

def current_time_stamp():
    return int(time())

def send_logs_to_kafka(input_log, output_log, producer):
    '''
    Publish input_log and output_log to kafka topics olorin_input_logs and olorin_output_logs respectively.
      These brokers are only for outputting to the visualizer Logstalgia. 
    '''
    producer.send('olorin_input_logs', input_log.encode('utf-8'))
    producer.flush()
    producer.send('olorin_output_logs', output_log.encode('utf-8'))
    producer.flush()

def post_ip_flag(ip, producer):
    '''
    Publish a flagged ip address to the kafka topic ip_flag
    '''
    producer.send('ip_flag', ip.encode('utf-8'))
    producer.flush()

def format_log_for_visualizer(log):
    '''
    Change the HTML response code. This is used to change the behavior of the visualizer, Logstalgia, and not 
      necessary for Olorin's flagging behavior. 
    '''
    return re.sub(' 429 ', ' 200 ', log)

def flag_check(ip, red):
    '''
    Check to see if the ip has been flagged.
    '''
    return red.get("flag{}".format(ip))

def flag_set(ip, time_stamp_sec, red):
    red.set("flag{}".format(ip), time_stamp_sec)

def tokens_set(ip, tokens, time_stamp, red):
    redis_value = "{},{}".format(tokens, time_stamp)
    red.set(ip, redis_value)

def update_tokens(tokens, last_time_stamp_sec, time_stamp_sec):
    new_token_value = tokens + ((time_stamp_sec - last_time_stamp_sec) // 2) - 1
    return max(0, new_token_value)

def update_or_create_ip_token(input_log, red, producer):
    '''
    input: input_log -> string -- raw apache log
           red       -> redis connection
           producer  -> kafka producer
    output: string -- formatted apache log used by the visualizer Logstalgia

    Check ip to see if it is flagged then update/create its token counter accordingly. Return the formatted 
      apache log for use by the visualizer Logstalgia.
    '''
    ip = get_ip(input_log)
    time_stamp_sec = convert_datetime_to_int(get_time_stamp(input_log))

    # check for flagged ip
    if flag_check(ip, red):
        flag_set(ip, time_stamp_sec, red)
        return format_log_for_visualizer(input_log)

    # update tokens and time stamp, flag if tokens == 0
    try:
        tokens, last_time_stamp_sec = [ int(num) for num in red.get(ip).decode('utf-8').split(',') ]
        new_token_value = update_tokens(tokens, last_time_stamp_sec, time_stamp_sec)
        tokens_set(ip, new_token_value, time_stamp_sec, red)

        if new_token_value == 0:
            flag_set(ip, time_stamp_sec, red)
            post_ip_flag(ip, producer)
            return format_log_for_visualizer(input_log)
        return input_log
    
    # create token entry for unregistered ip
    except:
        tokens_set(ip, TOKENS_MAX // 5, time_stamp_sec, red)
        return input_log        
        
    
def olorin_database_check(line):
    producer = KafkaProducer(bootstrap_servers = KAFKA_BROKERS)
    red = connect_to_redis()
    
    for row in line:
        if len(row[0]) > 0:
            output_log = update_or_create_ip_token(row[0], red, producer)
        else:
            output_log = row[0]
            
        send_logs_to_kafka(row[0], output_log, producer)

def olorin_main(ssc):
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

    print(OLORIN_ASCII_LOGO)

    olorin_main(ssc)
    ssc.start()
    ssc.awaitTermination()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() 
