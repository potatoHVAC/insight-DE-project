#!/usr/bin/env python3
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

def show_occasional(num):
    if int(num) % 3000 == 0:
        print(num)

def connect_to_menagerie():        
    conn = psycopg2.connect(host = POSTGRESQL_URL, database = DATABASE, user = POSTGRES_USER, password = POSTGRES_PASS)
    return (conn.cursor(), conn)

def sequential_menagerie_insert(line):
    cur, conn = connect_to_menagerie()
    for row in line:
        #show_occasional(row[0])
        print(row[0])
        sql = 'INSERT INTO sequential_menagerie(cc_number, observed) VALUES ({}, True);'.format(row[0])
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()
    

def transaction_main(sc, ssc):
    kafkaStream = KafkaUtils.createDirectStream(
        ssc,
        ['menagerie'],
        {'metadata.broker.list': KAFKA_BROKERS}
    )
    transaction = kafkaStream.map(lambda row: row[1].split(','))
    transaction.foreachRDD(lambda rdd: rdd.foreachPartition(show))

def sequential_main(sc, ssc):
    kafkaStreamSequential = KafkaUtils.createDirectStream(
        ssc,
        ['sequential-menagerie'],
        {'metadata.broker.list': KAFKA_BROKERS}
    )
    transactionSequential = kafkaStreamSequential.map(lambda row: row[1].split(','))
    transactionSequential.foreachRDD(lambda rdd: rdd.foreachPartition(sequential_menagerie_insert))
    
def main():
    sc = SparkContext(appName = APPNAME)
    sc.setLogLevel("WARN")
    ssc = StreamingContext(sc, 1)

    print(r''' 
     __________             __                                             
     \____    /____   ____ |  | __ ____   ____ ______   ___________  ______
       /     //  _ \ /  _ \|  |/ // __ \_/ __ \\____ \_/ __ \_  __ \/  ___/
      /     /(  <_> |  <_> )    <\  ___/\  ___/|  |_> >  ___/|  | \/\___ \ 
     /_______ \____/ \____/|__|_ \\___  >\___  >   __/ \___  >__|  /____  >
             \/                 \/    \/     \/|__|        \/           \/ 
                    _____  .__              .__                
                   /     \ |__| ______ _____|__| ____    ____  
                  /  \ /  \|  |/  ___//  ___/  |/    \  / ___\ 
                 /    Y    \  |\___ \ \___ \|  |   |  \/ /_/  >
                 \____|__  /__/____  >____  >__|___|  /\___  / 
                         \/        \/     \/        \//_____/  
           _____                                            .__        
          /     \   ____   ____ _____     ____   ___________|__| ____  
         /  \ /  \_/ __ \ /    \\__  \   / ___\_/ __ \_  __ \  |/ __ \ 
        /    Y    \  ___/|   |  \/ __ \_/ /_/  >  ___/|  | \/  \  ___/ 
        \____|__  /\___  >___|  (____  /\___  / \___  >__|  |__|\___  >
                \/     \/     \/     \//_____/      \/              \/ 
    ''')
    

    transaction_main(sc, ssc)
    sequential_main(sc, ssc)
    ssc.start()
    ssc.awaitTermination()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() 
