#!/usr/bin/env python3
#spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.1 sequential_consumer.py

import os
import re
import sys
import psycopg2
from time import sleep
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

SPARK_MASTER = 'ec2-35-165-101-226.us-west-2.compute.amazonaws.com'
APPNAME = 'SawThing'
KAFKA_BROKERS = 'ec2-34-215-153-129.us-west-2.compute.amazonaws.com:9092,ec2-52-36-50-195.us-west-2.compute.amazonaws.com:9092,ec2-52-88-169-142.us-west-2.compute.amazonaws.com:9092,ec2-54-71-226-161.us-west-2.compute.amazonaws.com:9092'
POSTGRESQL_URL = 'ec2-34-220-244-192.us-west-2.compute.amazonaws.com'
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASS = os.environ['POSTGRES_PASS']
DATABASE = 'menagerie'
TOKEN_MAX = 100

def connect_to_menagerie():        
    conn = psycopg2.connect(host = POSTGRESQL_URL,
                            database = DATABASE,
                            user = POSTGRES_USER,
                            password = POSTGRES_PASS)
    return (conn.cursor(), conn)

def get_ip(log):
    return re.match('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log).group(0)

def get_date(log):
    return re.findall('\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2}', log)[0]

def saw_menagerie_insert(line):
    cur, conn = connect_to_menagerie()
    for row in line:
        ip = get_ip(row[0])
        print(ip)
        date = get_date(row[0])
        print(date)
        #cur.execute(sql)
        #conn.commit()
    cur.close()
    conn.close()

def saw_main(sc, ssc):
    kafkaStreamSaw = KafkaUtils.createDirectStream(
        ssc,
        ['apache_logs'],
        {'metadata.broker.list': KAFKA_BROKERS}
    )
    transactionSaw = kafkaStreamSaw.map(lambda row: row[1].split(','))
    transactionSaw.foreachRDD(lambda rdd: rdd.foreachPartition(saw_menagerie_insert))
    
def main():
    sc = SparkContext(appName = APPNAME)
    sc.setLogLevel("WARN")
    ssc = StreamingContext(sc, 1)

    print(r''' 






    WE ARE UNDER ATTACK!!! MAN THE GIANT SAW THING!!!






    ''')

    saw_main(sc, ssc)
    ssc.start()
    ssc.awaitTermination()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() 
