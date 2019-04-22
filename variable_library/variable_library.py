APPNAME = 'Olorin'

SPARK_MASTER = '10.0.29.178'

DATABASE_IP = '10.0.55.99'
POSTGRESQL_DATABASE_NAME = 'menagerie'

KAFKA_BROKERS = '10.0.22.192:9092,10.0.47.91:9092,10.0.44.91:9092,10.0.8.67:9092'

MAIN_KAFKA_TOPIC = 'apache_logs'
OLORIN_KAFKA_INPUT_TOPIC = 'olorin_input_logs'
OLORIN_KAFKA_OUTPUT_TOPIC = 'olorin_output_logs'

APACHE_MESSAGES_FILE = 's3://speerd-bucket/apache_messages.txt'

OLORIN_ASCII_LOGO = r''' 





                    ________  .__               .__        
                    \_____  \ |  |   __/________|__| ____  
                     /   |   \|  |  /  _ \_  __ \  |/    \ 
                    /    |    \  |_(  <_> )  | \/  |   |  \
                    \_______  /____/\____/|__|  |__|___|  /
                            \/                          \/ 





    '''
