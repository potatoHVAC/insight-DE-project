#!/usr/bin/env python3

import os
import re
import sys
import datetime
from kafka import KafkaProducer
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from math import floor

from variable_library import (
    SPARK_MASTER,
    APPNAME,
    KAFKA_BROKERS,
)

CREDITS_MAX = 100

def get_ip(raw_log):
    return re.findall('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', raw_log)[0]

def get_time_stamp(raw_log):
    time_stamp_string = re.findall('\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2}', raw_log)[0]
    return datetime.datetime.strptime(time_stamp_string, '%d/%b/%Y:%H:%M:%S')

def send_logs_to_kafka(input_log, output_log, producer):
    producer.send('olorin_input_logs', input_log.encode('utf-8'))
    producer.flush()
    producer.send('olorin_output_logs', output_log.encode('utf-8'))
    producer.flush()

def format_log_for_visualizer(log):
    return re.sub(' 429 ', ' 200 ', log)
    
def olorin_database_check(line):
    producer = KafkaProducer(bootstrap_servers = KAFKA_BROKERS)    
    
    for row in line:
        ip = get_ip(row[0])
        time_stamp = get_time_stamp(row[0])

def olorin_main(sc, ssc):
    kafkaStreamSaw = KafkaUtils.createDirectStream(
        ssc,
        ['apache_logs'],
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
