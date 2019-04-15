#!/usr/bin/env python3

import os
import re
import sys
import psycopg2
import datetime
from kafka import KafkaProducer
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from math import floor

from variable_library import (
    SPARK_MASTER,
    APPNAME,
    KAFKA_BROKERS,
    POSTGRESQL_URL,
    DATABASE_NAME
)

POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASS = os.environ['POSTGRES_PASS']
CREDITS_MAX = 100

def connect_to_menagerie():        
    conn = psycopg2.connect(
        host = POSTGRESQL_URL,
        database = DATABASE_NAME,
        user = POSTGRES_USER,
        password = POSTGRES_PASS
    )
    return (conn.cursor(), conn)

def get_ip(raw_log):
    return re.findall('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', raw_log)[0]

def get_time_stamp(raw_log):
    time_stamp_string = re.findall('\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2}', raw_log)[0]
    return datetime.datetime.strptime(time_stamp_string, '%d/%b/%Y:%H:%M:%S')

def update_or_create_ip_entry(ip, time_stamp, cur, log, producer):
    cur.execute('SELECT credits, last_event FROM ip WHERE ip = %s', [ip])
    ip_row = cur.fetchall()

    output_log = log

    if len(ip_row) == 0:
        cur.execute('INSERT INTO ip (ip, credits, last_event) values (%s, %s, %s);',
                    [ip, CREDITS_MAX // 10, time_stamp])
    elif blacklisted_ip(ip, time_stamp, cur):
        output_log = format_log_for_visualizer(log)
    else:
        cur.execute('SELECT credits, last_event FROM ip WHERE ip = %s;', [ip])
        ip_credits, last_event = cur.fetchall()[0]
        update_ip_credits(ip, time_stamp, ip_credits, last_event, cur)
    send_logs_to_kafka(log, output_log, producer)

def send_logs_to_kafka(log, output_log, producer):
    producer.send('olorin_input_logs', log.encode('utf-8'))
    producer.flush()
    producer.send('olorin_output_logs', output_log.encode('utf-8'))
    producer.flush()

def format_log_for_visualizer(log):
    return re.sub(' 429 ', ' 200 ', log)
    
def blacklisted_ip(ip, time_stamp, cur, add_to_list = False):
    cur.execute('SELECT * FROM blacklist WHERE ip = %s;', [ip])
    blacklist_row = cur.fetchall()

    if len(blacklist_row) == 0:
        if add_to_list:
            cur.execute('UPDATE ip SET credits = 0, last_event = %s WHERE ip = %s;', [time_stamp, ip])
            cur.execute('INSERT INTO blacklist(ip, last_event) VALUES (%s, %s);', [ip, time_stamp])
        else:
            return False
    else:
        cur.execute('UPDATE blacklist SET last_event = %s WHERE ip = %s;', [time_stamp, ip])
        return True
        
def update_ip_credits(ip, time_stamp, ip_credits, last_event, cur):
    delta_time_sec = int(floor((time_stamp - last_event).total_seconds()))
    new_credits = max(-3600, min(ip_credits - 1 + (delta_time_sec // 2), CREDITS_MAX))

    if new_credits <= 0:
        blacklisted_ip(ip, time_stamp, cur, True)
    else:
        cur.execute('UPDATE ip SET credits = %s, last_event = %s WHERE ip = %s;', [new_credits, time_stamp, ip])

def olorin_database_check(line):
    cur, conn = connect_to_menagerie()
    producer = KafkaProducer(bootstrap_servers = KAFKA_BROKERS)    
    
    for row in line:
        ip = get_ip(row[0])
        time_stamp = get_time_stamp(row[0])
        update_or_create_ip_entry(ip, time_stamp, cur, row[0], producer)
        conn.commit()
    cur.close()
    conn.close()

def olorin_main(sc, ssc):
    kafkaStreamSaw = KafkaUtils.createDirectStream(
        ssc,
        ['apache_logs'],
        {'metadata.broker.list': KAFKA_BROKERS}
    )
    transactionSaw = kafkaStreamSaw.map(lambda row: row[1].split(','))
    transactionSaw.foreachRDD(lambda rdd: rdd.foreachPartition(olorin_database_check))
    
def main():
    sc = SparkContext(appName = APPNAME)
    sc.setLogLevel("WARN")
    ssc = StreamingContext(sc, 1)

    print(r''' 





                    ________  .__               .__        
                    \_____  \ |  |   __/________|__| ____  
                     /   |   \|  |  /  _ \_  __ \  |/    \ 
                    /    |    \  |_(  <_> )  | \/  |   |  \
                    \_______  /____/\____/|__|  |__|___|  /
                            \/                          \/ 





    ''')

    olorin_main(sc, ssc)
    ssc.start()
    ssc.awaitTermination()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() 
