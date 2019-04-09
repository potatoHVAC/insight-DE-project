#!/usr/bin/env python3

from time import time
from datetime import datetime
from random import randint
from smart_open import smart_open

MALICIOUS_IP = 's3://speerd-bucket/malicious_ip.txt'
FRIENDLY_IP = 's3://speerd-bucket/friendly_ip.txt'
APACHE_MESSAGE = 's3://speerd-bucket/apache_messages.txt'
APACHE_LOGS = 's3://speerd-bucket/apache_logs.txt'
GENERATOR_LOGS = 's3://speerd-bucket/generator_logs.txt'

CYCLES_SEC = 2000

def build_array_from(file_location):
    return [str(line.strip()) for line in smart_open(file_location, 'r')]

def format_log(ip, time, message):
    formated_time = datetime.fromtimestamp(time).strftime('%d/%h/%Y:%T')
    return ("{} - - [{} -0800] \"{}\n".format(ip, formated_time, message))

def generate_random_log(ips, time, messages):
    ip = ips[randint(0, len(ips) - 1)]
    message = messages[randint(0, len(messages) - 1)]
    return format_log(ip, time, message)

def generate_logs(ips, time_stamp, messages, chance):
    logs = []
    
    for index, ip_count in enumerate(ips):
        if random_chance(chance):
            logs.append(generate_random_log([ip_count[0]], time_stamp, messages))
            ips[index] = (ip_count[0], ip_count[1] - 1)
            
    ips = [ ip_count for ip_count in ips if ip_count[1] > 0 ]
    return (logs, ips)
    
def random_chance(scale):
    if randint(1,scale) == 1:
        return True
    else:
        return False

def post_logs(logs, destination_file):
    if logs:
        for log in logs:
            destination_file.write(str(log))

def activate_ips(active_ips, ips_history, ips_available, up_to, multiplier, chance):
    if random_chance(chance):
        number_to_reach = len(active_ips) + randint(1, up_to)
        
        while len(active_ips) < number_to_reach and len(active_ips) <= len(ips_available) // 2:
            new_ip = ips_available[randint(0, len(ips_available) - 1)]
            active_ips.append((new_ip, randint(10*multiplier, 30*multiplier)))
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
        
        if time_offset > 20 and time_offset < CYCLES_SEC - 400:
            active_ddos, ddos_history = activate_ips(
                active_ips = active_ddos,
                ips_history = ddos_history,
                ips_available = malicious_ips,
                up_to = 10,
                multiplier = 10,
                chance = 300
            )
                
        active_friendly, friendly_history = activate_ips(
            active_ips = active_friendly,
            ips_history = friendly_history,
            ips_available = friendly_ips,
            up_to = 3,
            multiplier = 1,
            chance = 4
        )
        
        ddos_logs, active_ddos = generate_logs(
            ips = active_ddos,
            time_stamp = start_time + time_offset,
            messages = messages,
            chance = 1
        )

        friendly_logs, active_friendly = generate_logs(
            ips = active_friendly,
            time_stamp = start_time + time_offset,
            messages = messages,
            chance = 3
        )

        post_logs(ddos_logs,  apache_log_file)
        post_logs(friendly_logs, apache_log_file)
        post_logs('*** cont: {} - friendly: {} - ddos: {} - friendly logs: {} - ddos logs: {} - total friendly: {} - total malicious: {}\n'.format(
            time_offset,
            len(active_friendly),
            len(active_ddos),
            len(friendly_logs),
            len(ddos_logs),
            len(friendly_history),
            len(ddos_history)
        ), generator_logs)
        time_offset += 1
        
main()
