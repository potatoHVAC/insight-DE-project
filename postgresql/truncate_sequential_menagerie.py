#!/usr/bin/env python3

import os
import psycopg2

POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASS = os.environ['POSTGRES_PASS']
DATABASE = 'menagerie'

def truncate_sequential_menagerie():        
    conn = psycopg2.connect(host = 'localhost', database = DATABASE, user = POSTGRES_USER, password = POSTGRES_PASS)
    cur = conn.cursor()
    cur.execute('TRUNCATE sequential_menagerie;')
    conn.commit()
    cur.close()
    conn.close()

def main():
    truncate_sequential_menagerie()

main()
