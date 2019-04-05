#!/bin/bash

# producer 
scp -i ~/.ssh/daniel-IAM-keypair.pem ./producer/sequential_producer.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./producer/s3_producer.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./data/generate_transactions.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/

# kafka
scp -i ~/.ssh/daniel-IAM-keypair.pem ./kafka/perturb_zookeeper.sh ubuntu@ec2-34-215-153-129.us-west-2.compute.amazonaws.com:~/

# spark
scp -i ~/.ssh/daniel-IAM-keypair.pem ./spark/consumer.py ubuntu@ec2-35-165-101-226.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./spark/start_consumer.sh ubuntu@ec2-35-165-101-226.us-west-2.compute.amazonaws.com:~/

# postgresql
scp -i ~/.ssh/daniel-IAM-keypair.pem ./postgresql/sql_differential_query.py ubuntu@ec2-34-220-244-192.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./postgresql/truncate_sequential_menagerie.py ubuntu@ec2-34-220-244-192.us-west-2.compute.amazonaws.com:~/
