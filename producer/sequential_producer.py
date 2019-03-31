#!/usr/bin/env python

import sys
from kafka import KafkaProducer

KAFKA_TOPIC = 'menagerie'
KAFKA_BROKERS = 'ec2-52-39-96-200.us-west-2.compute.amazonaws.com:9092,ec2-54-190-33-242.us-west-2.compute.amazonaws.com:9092,ec2-52-43-141-42.us-west-2.compute.amazonaws.com:9092,ec2-34-217-198-217.us-west-2.compute.amazonaws.com:9092'

def get_max_range():
    
    max_range_input = input("Maximum range [100,000]: ")
    
    try:
        return(int(max_range_input))
    except:
        return(100000)

def produce(max_range_int, brokers, topic):

    producer = KafkaProducer(bootstrap_servers = brokers)
    
    for i in range(max_range_int):
        producer.send(topic, str(i))
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
