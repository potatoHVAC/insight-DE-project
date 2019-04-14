#!/usr/bin/env python3

import sys
from kafka import KafkaConsumer
import datetime
from time import time

KAFKA_TOPIC = 'olorin_input_logs'
KAFKA_BROKERS = (
    'ec2-35-166-218-236.us-west-2.compute.amazonaws.com:9092,\
    ec2-52-39-44-29.us-west-2.compute.amazonaws.com:9092,\
    ec2-52-26-62-125.us-west-2.compute.amazonaws.com:9092,\
    ec2-52-32-145-50.us-west-2.compute.amazonaws.com:9092'
)

def consume(brokers, topic):

    consumer = KafkaConsumer(topic, bootstrap_servers=brokers, auto_offset_reset='latest')
    count_log = open('./olorin_input_count.log', 'a')

    count = 0
    for message in consumer:
        if count % 1000 == 0:
            current_time = datetime.datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')
            count_log.write('{} messages processed by \n'.format(count, current_time))
        print(message.value)
        count += 1
        
def main():
    consume(KAFKA_BROKERS, KAFKA_TOPIC)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()   
