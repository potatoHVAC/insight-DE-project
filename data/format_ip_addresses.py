import re
from random import randint
from smart_open import smart_open

MALICIOUS_IP = 's3://speerd-bucket/malicious_ip.txt'
FRIENDLY_IP = 's3://speerd-bucket/friendly_ip.txt'
RAW_IP = 's3://speerd-bucket/ips.txt'

def extract_ip_addresses(raw_ip_data):
    regex = '\d+\.\d+\.\d+\.\d+'
    return re.findall(regex, raw_ip_data)

def insert_ip_addresses(file_1, file_2, ips):
    for ip in ips:
        if randint(0,4) == 0:
            file_1.write(ip + '\n')
        else:
            file_2.write(ip + '\n')
            
def main():
    malicious_ip = smart_open(MALICIOUS_IP, 'w')
    frendly_ip = smart_open(FRIENDLY_IP, 'w')
    raw_ip = smart_open(RAW_IP, 'r')

    for line in raw_ip:
        ips = extract_ip_addresses(line)
        insert_ip_addresses(malicious_ip, frendly_ip, ips)

main()
