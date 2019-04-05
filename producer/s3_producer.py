#!/usr/bin/env python3

import sys
from kafka import KafkaProducer
from smart_open import smart_open

KAFKA_BUCKET = 's3://speerd-bucket/hundred_thousand_transactions.txt'
KAFKA_TOPIC = 'menagerie'
KAFKA_BROKERS = 'ec2-34-215-153-129.us-west-2.compute.amazonaws.com:9092,ec2-52-36-50-195.us-west-2.compute.amazonaws.com:9092,ec2-52-88-169-142.us-west-2.compute.amazonaws.com:9092,ec2-54-71-226-161.us-west-2.compute.amazonaws.com:9092'

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
