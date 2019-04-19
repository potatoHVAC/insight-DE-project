#!/usr/bin/env python3

import sys
from consumer_methods import *
from variable_library import (
    OLORIN_KAFKA_OUTPUT_TOPIC,
    KAFKA_BROKERS
)

LOG_FILE = './producer_logs/ip.log'

def main():
    consumer = KafkaConsumer('ip_flag', bootstrap_servers=KAFKA_BROKERS, auto_offset_reset='latest')
    for message in consumer:
        ip_list = open(LOG_FILE, 'a')

        ip_list.write('{}\n'.format(message.value))
        ip_list.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()   
