#!/bin/bash

# producer 
scp -i ~/.ssh/daniel-IAM-keypair.pem ../olorin/producer-node/friendly_producer.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ../olorin/producer-node/ddos_producer.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ../olorin/producer-node/ip_methods.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/

# kafka

# spark
scp -i ~/.ssh/daniel-IAM-keypair.pem ../olorin/spark-node/postgresql_consumer.py ubuntu@ec2-35-165-101-226.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ../olorin/spark-node/postgresql_start_consumer.sh ubuntu@ec2-35-165-101-226.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ../olorin/spark-node/redis_consumer.py ubuntu@ec2-35-165-101-226.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ../olorin/spark-node/redis_start_consumer.sh ubuntu@ec2-35-165-101-226.us-west-2.compute.amazonaws.com:~/

# database

# visualizer

scp -i ~/.ssh/daniel-IAM-keypair.pem ../olorin/visualizer-node/olorin.py ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ../olorin/visualizer-node/input_consumer.py ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ../olorin/visualizer-node/output_consumer.py ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ../olorin/visualizer-node/consumer_methods.py ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ../olorin/visualizer-node/ip_consumer.py ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com:~/
