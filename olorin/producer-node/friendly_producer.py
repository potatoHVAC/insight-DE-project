#!/usr/bin/env python3

import sys
from ip_methods import *
from variable_library import ( 
    MAIN_KAFKA_TOPIC,
    KAFKA_BROKERS,
    APACHE_MESSAGES_FILE
)

MAX_IPS = 500
SLEEP_INTERVAL = 0.1

def main():
    producer = KafkaProducer(bootstrap_servers = KAFKA_BROKERS)
    log_file = open('./friendly_ip_producer.log', 'a')
    available_messages = build_array_from(APACHE_MESSAGES_FILE)[:50]

    active_ips = {}
    apache_logs = []
    log_count = 0
    while True:

        if len(active_ips) < MAX_IPS:
            active_ips = activate_ips(
                active_ips = active_ips,
                number_to_activate = MAX_IPS,
                last_ip_num_range = [0,150]
            )

        active_ips, apache_logs = generate_logs(active_ips, available_messages)
        log_count += len(apache_logs)
        produce_messages(apache_logs, producer, MAIN_KAFKA_TOPIC)
        post_generator_log(active_ips, apache_logs, log_count, log_file)

        sleep(SLEEP_INTERVAL)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
