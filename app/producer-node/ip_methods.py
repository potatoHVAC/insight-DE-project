
from time import (time, sleep)
from random import randint
from datetime import datetime
from kafka import KafkaProducer
from smart_open import smart_open

def build_array_from(file_location):
    return [str(line.strip()) for line in smart_open(file_location, 'r')]

def activate_ips(active_ips, number_to_activate, last_ip_num_range, is_ddos = False):
    target = len(active_ips) + number_to_activate

    while len(active_ips) < target:
        new_ip = generate_ip(last_ip_num_range)
        if is_ddos:
            active_ips[new_ip] = 500
        else:
            active_ips[new_ip] = randint(5, 30)
        
    return active_ips

def generate_logs(active_ips, available_messages, is_ddos = False):
    apache_logs = []

    for ip, log_counter in active_ips.items():
        if random_chance(randint(15,40)) or is_ddos:
            apache_logs.append(format_log(ip, available_messages))
            active_ips[ip] -= 1

    active_ips = { ip: log_counter for ip, log_counter in active_ips.items() if log_counter > 0 }
    
    return (active_ips, apache_logs)

def format_log(ip, available_messages):
    message = available_messages[randint(0, len(available_messages) -1)]
    return "{} - - [{} -0800] {}\n".format(ip, time_stamp(), message)
    
def time_stamp():
    return datetime.fromtimestamp(time()).strftime('%d/%h/%Y:%T')    

def produce_messages(apache_logs, producer, topic):
    for log in apache_logs:
        producer.send(topic, log.encode('utf-8'))
        producer.flush()

def post_generator_log(active_ips, logs, log_count, log_file):
    generator_log = "active IPs: {} -- logs: {} -- total logs: {} -- {}\n"\
          .format(len(active_ips), len(logs), log_count, time_stamp())
    log_file.write(generator_log)
    log_file.close

def random_chance(scale):
    return randint(1,scale) == 1

def generate_ip(last_num_range):
    return "{}.{}.{}.{}".format(
        randint(0,255),
        randint(0,255),
        randint(0,255),
        randint(last_num_range[0], last_num_range[1])
    )

