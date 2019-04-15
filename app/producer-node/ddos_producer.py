#!/usr/bin/env python3

import sys
from ip_methods import *
from variable_library import (
    MAIN_KAFKA_TOPIC,
    KAFKA_BROKERS,
    APACHE_MESSAGES_FILE
)

NUMBER_OF_DDOS_NODES = 10
NUMBER_OF_DDOS_TARGETS = 3
SLEEP_INTERVAL = 0.05

def main():
    producer = KafkaProducer(bootstrap_servers = KAFKA_BROKERS)
    log_file = open('./producer_logs/friendly_ip_producer.log', 'a')
    available_messages = build_array_from(APACHE_MESSAGES_FILE)[:NUMBER_OF_DDOS_TARGETS]

    active_ips = activate_ips(
        active_ips = {},
        number_to_activate = NUMBER_OF_DDOS_NODES,
        last_ip_num_range = [151,255],
        is_ddos = True
    )
    apache_logs = []
    log_count = 0
    while True:

        active_ips, apache_logs = generate_logs(
            active_ips,
            available_messages,
            is_ddos = True
        )
        log_count += len(apache_logs)
        produce_messages(apache_logs, producer, MAIN_KAFKA_TOPIC)
        post_generator_log(active_ips, apache_logs, log_count, log_file)

        sleep(SLEEP_INTERVAL)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
