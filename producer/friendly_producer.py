#!/usr/bin/env python3

import sys
from ip_methods import *

MAX_IPS = 500
APACHE_MESSAGES = 's3://speerd-bucket/apache_messages.txt'
KAFKA_TOPIC = 'apache_logs'
SLEEP_INTERVAL = 0.1
KAFKA_BROKERS = (
    'ec2-35-166-218-236.us-west-2.compute.amazonaws.com:9092,\
    ec2-52-39-44-29.us-west-2.compute.amazonaws.com:9092,\
    ec2-52-26-62-125.us-west-2.compute.amazonaws.com:9092,\
    ec2-52-32-145-50.us-west-2.compute.amazonaws.com:9092'
)

def main():
    producer = KafkaProducer(bootstrap_servers = KAFKA_BROKERS)
    log_file = open('./producer_logs/friendly_ip_producer.log', 'a')
    available_messages = build_array_from(APACHE_MESSAGES)[:50]

    active_ips = {}
    apache_logs = []
    log_count = 0
    while True:

        if len(active_ips) < MAX_IPS:
            active_ips = activate_ips(
                active_ips = active_ips,
                number_to_activate = 1,
                last_ip_num_range = [0,150]
            )

        active_ips, apache_logs = generate_logs(active_ips, available_messages)
        log_count += len(apache_logs)
        produce_messages(apache_logs, producer, 'apache_logs')
        post_generator_log(active_ips, apache_logs, log_count, log_file)

        sleep(SLEEP_INTERVAL)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
