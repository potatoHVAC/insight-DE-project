#!/usr/bin/env python3

import sys
from kafka import KafkaProducer
from smart_open import smart_open

S3_BUCKET = 's3://speerd-bucket/apache_logs.txt'
KAFKA_TOPIC = 'apache_logs'
KAFKA_BROKERS = (
    'ec2-35-166-218-236.us-west-2.compute.amazonaws.com:9092,\
    ec2-52-39-44-29.us-west-2.compute.amazonaws.com:9092,\
    ec2-52-26-62-125.us-west-2.compute.amazonaws.com:9092,\
    ec2-52-32-145-50.us-west-2.compute.amazonaws.com:9092'
)

def produce(bucket, brokers, topic):

    producer = KafkaProducer(bootstrap_servers = brokers)

    for line in smart_open(bucket, 'r'):
        producer.send(topic, line.strip().encode('utf-8'))
        producer.flush()
        
def main():
    produce(S3_BUCKET, KAFKA_BROKERS, KAFKA_TOPIC)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
