
from kafka import KafkaConsumer
from datetime import datetime
from time import time

def time_stamp():
    return datetime.fromtimestamp(time()).strftime('%d/%h/%Y:%T')    

def post_log(count, last_time, log_file):
    count_log = open(log_file, 'a')
    current_time = time()
    count_log.write('{} messages in {} seconds, processed by {}\n'\
                    .format(count, str(current_time - last_time)[:5], time_stamp()))
    count_log.close()
    return current_time   
    
def consume(brokers, topic, log_file):

    consumer = KafkaConsumer(topic, bootstrap_servers=brokers, auto_offset_reset='latest')

    count = 0
    last_time = time()
    for message in consumer:
        if count % 1000 == 0:
            last_time = post_log(count, last_time, log_file)
        print(message.value)
        count += 1
