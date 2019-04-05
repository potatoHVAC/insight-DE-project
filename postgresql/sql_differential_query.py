#!/usr/bin/env python3

import os
import sys
import psycopg2
from time import sleep, time
import datetime

POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASS = os.environ['POSTGRES_PASS']
DATABASE = 'menagerie'

def sql_differential_check():        
    conn = psycopg2.connect(host = 'localhost', database = DATABASE, user = POSTGRES_USER, password = POSTGRES_PASS)
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) AS Total, (SELECT cc_number FROM sequential_menagerie ORDER BY cc_number DESC LIMIT 1) AS top, COUNT(*) - 1 - (SELECT cc_number FROM sequential_menagerie ORDER BY cc_number DESC LIMIT 1) AS diff FROM sequential_menagerie;')
    results = cur.fetchall()    
    cur.close()
    conn.close()
    return results

def main():
    while True:
        current_time = datetime.datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')
        print('Check performed at: {}'.format(current_time))
        print(sql_differential_check())
        sleep(5)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() 


