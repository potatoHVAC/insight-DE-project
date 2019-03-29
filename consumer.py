1import sys
from kafka import KafkaConsumer

KAFKA_TOPIC = 'test-topic'
KAFKA_BROKERS = 'ec2-35-166-204-26.us-west-2.compute.amazonaws.com:9092'



consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BROKERS,
                         auto_offset_reset='earliest')



try:
    for message in consumer:
        print(message.value.decode('utf-8'))
except KeyboardInterrupt:
    sys.exit()
