#!/bin/bash

# producer 
scp -i ~/.ssh/daniel-IAM-keypair.pem ./app/producer-node/friendly_producer.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./app/producer-node/ddos_producer.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./app/producer-node/ip_methods.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/

# kafka

# spark
scp -i ~/.ssh/daniel-IAM-keypair.pem ./data-processing/consumer.py ubuntu@ec2-35-165-101-226.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./data-processing/start_consumer.sh ubuntu@ec2-35-165-101-226.us-west-2.compute.amazonaws.com:~/

# database

# dash

scp -i ~/.ssh/daniel-IAM-keypair.pem ./app/dash-node/olorin.py ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./app/dash-node/input_consumer.py ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./app/dash-node/output_consumer.py ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./app/dash-node/consumer_methods.py ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com:~/
