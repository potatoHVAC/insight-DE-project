#!/usr/bin/env python3

import sys
from producer_methods import *
from variable_library import (
    MAIN_KAFKA_TOPIC,
    KAFKA_BROKERS,
    APACHE_MESSAGES_FILE
)

NUMBER_OF_DDOS_NODES = 100
NUMBER_OF_DDOS_TARGETS = 5
SLEEP_INTERVAL = 0.05

def main(rate_limit, record_log):
    producer = KafkaProducer(bootstrap_servers = KAFKA_BROKERS)
    log_file = open('./ddos_ip_producer.log', 'a')
    available_messages = build_array_from(APACHE_MESSAGES_FILE)[:NUMBER_OF_DDOS_TARGETS]

    active_ips = activate_ips(
        active_ips = {},
        number_to_activate = NUMBER_OF_DDOS_NODES,
        last_ip_num_range = [151,255],
        ddos_message_count = 10000000
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

        if rate_limit:
            sleep(SLEEP_INTERVAL)
        if record_log:
            post_generator_log(active_ips, apache_logs, log_count, log_file)

if __name__ == '__main__':
    try:
        main(rate_limit = False, record_log = False)
    except KeyboardInterrupt:
        sys.exit()
