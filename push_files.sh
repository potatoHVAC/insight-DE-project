#!/bin/bash

# producer 
#scp -i ~/.ssh/daniel-IAM-keypair.pem ./producer/s3_producer.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/old/
#scp -i ~/.ssh/daniel-IAM-keypair.pem ./data/apache_log_generator.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/old/
#scp -i ~/.ssh/daniel-IAM-keypair.pem ./data/format_ip_addresses.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/old/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./producer/friendly_producer.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./producer/ddos_producer.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./producer/ip_methods.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/

# kafka

# spark
scp -i ~/.ssh/daniel-IAM-keypair.pem ./spark/consumer.py ubuntu@ec2-35-165-101-226.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./spark/start_consumer.sh ubuntu@ec2-35-165-101-226.us-west-2.compute.amazonaws.com:~/

# postgresql

# dash

scp -i ~/.ssh/daniel-IAM-keypair.pem ./dash/olorin.py ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./dash/input_consumer.py ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./dash/output_consumer.py ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./dash/consumer_methods.py ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com:~/
