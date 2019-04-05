#!/usr/bin/env python3

import sys
from kafka import KafkaProducer

KAFKA_TOPIC = 'sequential-menagerie'
KAFKA_BROKERS = 'ec2-34-215-153-129.us-west-2.compute.amazonaws.com:9092,ec2-52-36-50-195.us-west-2.compute.amazonaws.com:9092,ec2-52-88-169-142.us-west-2.compute.amazonaws.com:9092,ec2-54-71-226-161.us-west-2.compute.amazonaws.com:9092'

def get_max_range():

    try:
        max_range_input = int(input("Maximum range [1,000,000,000]: "))
    except:
        max_range_input = 1000000000
    return max_range_input

def produce(max_range_int, brokers, topic):

    producer = KafkaProducer(bootstrap_servers = brokers)
    
    for i in range(max_range_int):
        producer.send(topic, str(i).encode('utf-8'))
        producer.flush()
        if i % 1000 == 0:
            print (i)

def main():
    max_range = get_max_range()
    produce(max_range, KAFKA_BROKERS, KAFKA_TOPIC)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
