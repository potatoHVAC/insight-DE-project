#!/usr/bin/env python3

from time import time
from datetime import datetime
from random import randint
from smart_open import smart_open

MALICIOUS_IP = 's3://speerd-bucket/malicious_ip.txt'
FRIENDLY_IP = 's3://speerd-bucket/friendly_ip.txt'
APACHE_MESSAGE = 's3://speerd-bucket/apache_messages.txt'
APACHE_LOGS = 's3://speerd-bucket/apache_logs100k.txt'
GENERATOR_LOGS = 's3://speerd-bucket/generator_logs100k.txt'

CYCLES_SEC = 100000

def build_array_from(file_location):
    return [str(line.strip()) for line in smart_open(file_location, 'r')]

def format_log(ip, time, message):
    formated_time = datetime.fromtimestamp(time).strftime('%d/%h/%Y:%T')
    return ("{} - - [{} -0800] \"{}\n".format(ip, formated_time, message))

def generate_random_log(ips, time, messages):
    ip = ips[randint(0, len(ips) - 1)]
    message = messages[randint(0, len(messages) - 1)]
    return format_log(ip, time, message)

def generate_ddos_logs(ips, time, messages):
    return [ generate_random_log([ip], time, messages) for ip, _ in ips ]

def generate_friendly_logs(ips, time, messages):
    friendly_logs = []
    for index, tup in enumerate(ips):
        if random_chance(3):
            friendly_logs.append(generate_random_log([tup[0]], time, messages))
            ips[index] = (tup[0], tup[1] - 1)
    ips = [ tup for tup in ips if tup[1] > 0 ]
    return (friendly_logs, ips)
    
def random_chance(scale):
    if randint(1,scale) == 1:
        return True
    else:
        return False

def post_logs(logs, destination_file):
    for log in logs:
        destination_file.write(str(log))

def advance_counter(ip_tuples):
    reduced_counter = list(map(lambda tup: (tup[0], tup[1] - 1), ip_tuples))
    return [ tup for tup in reduced_counter if tup[1] > 0 ]

def activate_ips(active_ips, ips_history, ips_available, count, multiplier):
    for i in range(randint(1,count)):
        new_ip = ips_available[randint(0, len(ips_available) - 1)]
        active_ips.append((new_ip, randint(3*multiplier, 50*multiplier)))
        ips_history.add(new_ip)
    return (active_ips, ips_history)        



def main():
    malicious_ips = build_array_from(MALICIOUS_IP)
    friendly_ips = build_array_from(FRIENDLY_IP)
    messages = build_array_from(APACHE_MESSAGE)
    apache_log_file = smart_open(APACHE_LOGS, 'w')
    generator_logs = smart_open(GENERATOR_LOGS, 'w')

    start_time = time()
    time_offset = 0
    active_ddos = []
    ddos_history = set()
    active_friendly = []
    friendly_history = set()

    while time_offset < CYCLES_SEC:

        if random_chance(2):
            active_friendly, friendly_history = activate_ips(
                active_friendly,
                friendly_history,
                friendly_ips,
                3,
                1
            )
        if random_chance(1000) and time_offset < CYCLES_SEC - 500:
            active_ddos, ddos_history = activate_ips(
                active_ddos,
                ddos_history,
                malicious_ips,
                5,
                10
            )
            
        ddos_logs = []
        friendly_logs = []
        if active_ddos:
            ddos_logs = generate_ddos_logs(active_ddos, start_time + time_offset, messages)
            post_logs(ddos_logs,  apache_log_file)
            active_ddos = advance_counter(active_ddos)
        if active_friendly:
            friendly_logs, active_friendly = generate_friendly_logs(
                active_friendly,
                start_time + time_offset,
                messages
            )
            post_logs(friendly_logs, apache_log_file)

        post_logs('*** cont: {} - friendly: {} - ddos: {} - friendly logs: {} - ddos logs: {}\n'.format(
            time_offset,
            len(active_friendly),
            len(active_ddos),
            len(friendly_logs),
            len(ddos_logs)
        ), generator_logs)
        time_offset += 1
        
main()
