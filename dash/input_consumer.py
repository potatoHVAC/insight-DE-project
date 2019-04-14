#!/usr/bin/env python3

import sys
from consumer_methods import *

KAFKA_TOPIC = 'olorin_input_logs'
LOG_FILE = './producer_logs/olorin_input_count.log'
KAFKA_BROKERS = (
    'ec2-35-166-218-236.us-west-2.compute.amazonaws.com:9092,\
    ec2-52-39-44-29.us-west-2.compute.amazonaws.com:9092,\
    ec2-52-26-62-125.us-west-2.compute.amazonaws.com:9092,\
    ec2-52-32-145-50.us-west-2.compute.amazonaws.com:9092'
)
        
def main():
    consume(KAFKA_BROKERS, KAFKA_TOPIC, LOG_FILE)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()   
