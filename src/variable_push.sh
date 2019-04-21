#!/bin/bash

# producer 
scp -i ~/.ssh/daniel-IAM-keypair.pem ${OLORIN_HOME}/variable_library/variable_library.py ubuntu@${PRODUCER_IP}:~/

# kafka

# spark
scp -i ~/.ssh/daniel-IAM-keypair.pem ${OLORIN_HOME}/variable_library/variable_library.py ubuntu@${SPARK_MASTER_IP}:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ${OLORIN_HOME}/variable_library/private_variable_library.py ubuntu@${SPARK_MASTER_IP}:~/

# database

# visualizer

scp -i ~/.ssh/daniel-IAM-keypair.pem ${OLORIN_HOME}/variable_library/variable_library.py ubuntu@${VISUALIZER_IP}:~/
