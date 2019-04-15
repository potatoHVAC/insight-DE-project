import os

APPNAME = 'Olorin'

SPARK_MASTER = 'ec2-35-165-101-226.us-west-2.compute.amazonaws.com'

POSTGRESQL_URL = 'ec2-34-220-244-192.us-west-2.compute.amazonaws.com'
DATABASE_NAME = 'menagerie'

KAFKA_BROKERS = (
    'ec2-35-166-218-236.us-west-2.compute.amazonaws.com:9092,\
    ec2-52-39-44-29.us-west-2.compute.amazonaws.com:9092,\
    ec2-52-26-62-125.us-west-2.compute.amazonaws.com:9092,\
    ec2-52-32-145-50.us-west-2.compute.amazonaws.com:9092'
)
MAIN_KAFKA_TOPIC = 'apache_logs'
OLORIN_KAFKA_INPUT_TOPIC = 'olorin_input_logs'
OLORIN_KAFKA_OUTPUT_TOPIC = 'olorin_output_logs'

APACHE_MESSAGES_FILE = 's3://speerd-bucket/apache_messages.txt'
