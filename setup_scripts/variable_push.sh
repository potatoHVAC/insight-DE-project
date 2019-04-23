#!/bin/bash

# producer Node
scp -i ~/.ssh/daniel-IAM-keypair.pem ${OLORIN_HOME}/variable_library/variable_library.py ubuntu@${PRODUCER_IP}:~/

# Kafka Node

# Spark Node
scp -i ~/.ssh/daniel-IAM-keypair.pem ${OLORIN_HOME}/variable_library/variable_library.py ubuntu@${SPARK_MASTER_IP}:~/
# the following script is used to push the private_variable_library to the Spark Master node. This library contains POSTGRES_USER and POSTGRES_PASS used in the PostgreSQL consumer. This is not currently supported in the setup procedure and has been commented out. 
#scp -i ~/.ssh/daniel-IAM-keypair.pem ${OLORIN_HOME}/variable_library/private_variable_library.py ubuntu@${SPARK_MASTER_IP}:~/

# Database Node

# Visualizer Node

scp -i ~/.ssh/daniel-IAM-keypair.pem ${OLORIN_HOME}/variable_library/variable_library.py ubuntu@${VISUALIZER_IP}:~/
