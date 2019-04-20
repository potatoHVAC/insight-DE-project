APPNAME = 'Olorin'

SPARK_MASTER = '10.0.0.10'

DATABASE_IP = '10.0.0.5'
POSTGRESQL_DATABASE_NAME = 'menagerie'

KAFKA_BROKERS = '10.0.0.6:9092,10.0.0.9:9092,10.0.0.13:9092,10.0.0.11:9092'

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
