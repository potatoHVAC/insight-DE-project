import sys
import random
from kafka import KafkaProducer

def main():

    producer = KafkaProducer(bootstrap_servers = 'ec2-35-166-204-26.us-west-2.compute.amazonaws.com:9092,ec2-34-215-148-32.us-west-2.compute.amazonaws.com:9092,ec2-34-218-22-168.us-west-2.compute.amazonaws.com:9092,ec2-34-210-33-59.us-west-2.compute.amazonaws.com:9092')


    for i in range(random.randint(1,20)):
	producer.send('test-topic', str(i).encode('utf-8'))
        producer.flush()
        print (i)

    return

if __name__ == '__main__':
    main()
