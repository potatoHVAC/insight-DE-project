#!/usr/bin/env python

import sys
from kafka import KafkaProducer
from smart_open import smart_open

KAFKA_BUCKET = 's3://speerd-bucket/random.txt'
KAFKA_TOPIC = 'menagerie'
KAFKA_BROKERS = 'ec2-52-39-96-200.us-west-2.compute.amazonaws.com:9092,ec2-54-190-33-242.us-west-2.compute.amazonaws.com:9092,ec2-52-43-141-42.us-west-2.compute.amazonaws.com:9092,ec2-34-217-198-217.us-west-2.compute.amazonaws.com:9092'

def produce(bucket, brokers, topic):

    producer = KafkaProducer(bootstrap_servers = brokers)

    for line in smart_open(bucket, 'r'):
        producer.send(topic, line.strip().encode('utf-8'))
        producer.flush()
        
def main():
    produce(KAFKA_BUCKET, KAFKA_BROKERS, KAFKA_TOPIC)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
