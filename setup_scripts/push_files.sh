#!/bin/bash

# producer 
scp -i ~/.ssh/daniel-IAM-keypair.pem ${OLORIN_HOME}/olorin/producer-node/friendly_producer.py ubuntu@${PRODUCER_IP}:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ${OLORIN_HOME}/olorin/producer-node/ddos_producer.py ubuntu@${PRODUCER_IP}:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ${OLORIN_HOME}/olorin/producer-node/producer_methods.py ubuntu@${PRODUCER_IP}:~/

# kafka

# spark
#scp -i ~/.ssh/daniel-IAM-keypair.pem ${OLORIN_HOME}/olorin/spark-node/postgresql_consumer.py ubuntu@${SPARK_MASTER_IP}:~/
#scp -i ~/.ssh/daniel-IAM-keypair.pem ${OLORIN_HOME}/olorin/spark-node/postgresql_start_consumer.sh ubuntu@${SPARK_MASTER_IP}:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ${OLORIN_HOME}/olorin/spark-node/redis_consumer.py ubuntu@${SPARK_MASTER_IP}:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ${OLORIN_HOME}/olorin/spark-node/redis_start_consumer.sh ubuntu@${SPARK_MASTER_IP}:~/

# database

# visualizer

scp -i ~/.ssh/daniel-IAM-keypair.pem ${OLORIN_HOME}/olorin/visualizer-node/input_consumer.py ubuntu@${VISUALIZER_IP}:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ${OLORIN_HOME}/olorin/visualizer-node/output_consumer.py ubuntu@${VISUALIZER_IP}:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ${OLORIN_HOME}/olorin/visualizer-node/consumer_methods.py ubuntu@${VISUALIZER_IP}:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ${OLORIN_HOME}/olorin/visualizer-node/ip_consumer.py ubuntu@${VISUALIZER_IP}:~/
