#!/usr/bin/env python

import sys
from kafka import KafkaConsumer

KAFKA_TOPIC = 'menagerie'
KAFKA_BROKERS = 'ec2-52-39-96-200.us-west-2.compute.amazonaws.com:9092,ec2-54-190-33-242.us-west-2.compute.amazonaws.com:9092,ec2-52-43-141-42.us-west-2.compute.amazonaws.com:9092,ec2-34-217-198-217.us-west-2.compute.amazonaws.com:9092'

def consume():

    consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BROKERS, auto_offset_reset='earliest')
    last_num = -1

    for message in consumer:

        num = int(message.value)

        if num % 100 == 0:
            print('just passed ' + str(num))
        if num != last_num + 1:
            print(str(last_num) + ' was missed')

        last_num = num

def main():
    consume()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()    
