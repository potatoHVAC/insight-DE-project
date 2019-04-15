APPNAME = 'Olorin'

SPARK_MASTER = 'ip-10-0-0-10.us-west-2.compute.internal'

POSTGRESQL_URL = 'ip-10-0-0-5.us-west-2.compute.internal'
DATABASE_NAME = 'menagerie'

KAFKA_BROKERS = (
    'ip-10-0-0-6.us-west-2.compute.internal:9092,\
    ip-10-0-0-9.us-west-2.compute.internal:9092,\
    ip-10-0-0-13.us-west-2.compute.internal:9092,\
    ip-10-0-0-11.us-west-2.compute.internal:9092'
)

MAIN_KAFKA_TOPIC = 'apache_logs'
OLORIN_KAFKA_INPUT_TOPIC = 'olorin_input_logs'
OLORIN_KAFKA_OUTPUT_TOPIC = 'olorin_output_logs'

APACHE_MESSAGES_FILE = 's3://speerd-bucket/apache_messages.txt'
