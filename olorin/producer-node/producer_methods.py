
from time import (time, sleep)
from random import randint
from datetime import datetime
from kafka import KafkaProducer
from smart_open import smart_open

def build_array_from(file_location):
    '''
    input: string -- file location
    output: list of strings -- list including each row of the target file as a seperate string entity
    '''
    return [str(line.strip()) for line in smart_open(file_location, 'r')]

def activate_ips(active_ips, number_to_activate, last_ip_num_range, ddos_message_count = 0):
    '''
    input: active_ips -> dict{ip: message count} -- message count is the remaining messages for that ip to send
           number_to_activate -> the number of ips that will activate
           last_ip_num_range -> [int, int] -- min and max values for the last number in ip address
           ddos_message_count -> int -- sets the ddos messages to all be the same
    output: active_ips -- updated with all new ips and their message counts

    Activates the desired number of ip addresses and adds them to the active_ips dictionary.
    '''
    
    target = len(active_ips) + number_to_activate
    while len(active_ips) < target:
        new_ip = generate_ip(last_ip_num_range)
        if ddos_message_count > 0:
            active_ips[new_ip] = ddos_message_count
        else:
            active_ips[new_ip] = randint(5, 30)
        
    return active_ips

def generate_logs(active_ips, available_messages, is_ddos = False):
    '''
    input: active_ips -> dict{ip: message count} -- message count is the remaining messages for that ip to send
           available_messages -> list of strings
           is_ddos -> boolean
    output: active_ips -- updated dictionary with reduced message count
            apache_logs -> list of strings

    Generates a list of all apache logs that occured in this time interval and updates the message 
      counters for all ips that sent a message.
    '''

    apache_logs = []
    for ip, log_counter in active_ips.items():
        if random_chance(randint(20, 30)) or is_ddos:
            apache_logs.append(format_log(ip, available_messages))
            active_ips[ip] -= 1

    active_ips = { ip: log_counter for ip, log_counter in active_ips.items() if log_counter > 0 }
    
    return (active_ips, apache_logs)

def format_log(ip, available_messages):
    '''
    input: ip -> string
           available_messages -> list of strings
    output: string -- formatted apache log
    '''
    message = available_messages[randint(0, len(available_messages) -1)]
    return "{} - - [{} -0800] {}\n".format(ip, time_stamp(), message)
    
def time_stamp():
    '''
    output: string -- formatted time stamp
    '''
    return datetime.fromtimestamp(time()).strftime('%d/%h/%Y:%T')    

def produce_messages(apache_logs, producer, topic):
    '''
    input: apache_logs -> list of strings
           producer    -> connection -- kafka producer
           topic       -> string     -- kafka topic

    Publishes a list of apache logs to the kafka brokers
    '''
    for log in apache_logs:
        producer.send(topic, log.encode('utf-8'))
        producer.flush()

def post_generator_log(active_ips, logs, log_count, log_file):
    '''
    Publishes a log with metrics for the apache log generation
    '''
    generator_log = "active IPs: {} -- logs: {} -- total logs: {} -- {}\n"\
          .format(len(active_ips), len(logs), log_count, time_stamp())
    log_file.write(generator_log)
    log_file.close

def random_chance(scale):
    return randint(1,scale) == 1

def generate_ip(last_num_range):
    '''
    input: [int, int] -- min and max integers for setting range on ip address
    output: string    -- formatted ip address
    '''

    return "{}.{}.{}.{}".format(
        randint(0,255),
        randint(0,255),
        randint(0,255),
        randint(last_num_range[0], last_num_range[1])
    )

