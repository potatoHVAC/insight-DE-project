#!/usr/bin/env python
#spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.1 sequential_consumer.py

import os
import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import psycopg2

SPARK_MASTER = 'ec2-34-216-31-151.us-west-2.compute.amazonaws.com'
APPNAME = 'ZookeepersMissingMenagerie'
KAFKA_BROKERS = 'ec2-52-39-96-200.us-west-2.compute.amazonaws.com:9092'#,ec2-54-190-33-242.us-west-2.compute.amazonaws.com:9092,ec2-52-43-141-42.us-west-2.compute.amazonaws.com:9092,ec2-34-217-198-217.us-west-2.compute.amazonaws.com:9092'
POSTGRESQL_URL = 'ec2-34-220-244-192.us-west-2.compute.amazonaws.com'
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASS = os.environ['POSTGRES_PASS']
DATABASE = 'menagerie'

def show(line):
    for l in line:
        print(l[0])
    

def main():
    sc = SparkContext(appName = APPNAME)
    sc.setLogLevel("WARN")
    ssc = StreamingContext(sc, 1)

    connection = psycopg2.connect(host = POSTGRESQL_URL, database = DATABASE, user = POSTGRES_USER, password = POSTGRES_PASS)
    cursor = connection.cursor()


    kafkaStream = KafkaUtils.createDirectStream(ssc, ['menagerie'], {'metadata.broker.list': KAFKA_BROKERS})
    kafkaStreamSequential = KafkaUtils.createDirectStream(ssc, ['sequential-menagerie'], {'metadata.broker.list': KAFKA_BROKERS})
    
    transaction = kafkaStream.map(lambda row: row[1].split(','))
    transactionSequential = kafkaStreamSequential.map(lambda row: row[1].split(','))
 
    transaction.foreachRDD(lambda rdd: rdd.foreachPartition(show))
    transactionSequential.foreachRDD(lambda rdd: rdd.foreachPartition(show))

    print('\n\n\n\n\n\n\n\nhi curtis\n\n\n\n\n\n\n\n')

    ssc.start()
    ssc.awaitTermination()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() 
