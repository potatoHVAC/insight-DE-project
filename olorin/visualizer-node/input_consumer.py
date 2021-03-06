#!/usr/bin/env python3

import sys
from consumer_methods import *
from variable_library import (
    OLORIN_KAFKA_INPUT_TOPIC,
    KAFKA_BROKERS
)

LOG_FILE = './producer_logs/olorin_input_count.log'
        
def main():
    consume(KAFKA_BROKERS, OLORIN_KAFKA_INPUT_TOPIC, LOG_FILE)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()   
