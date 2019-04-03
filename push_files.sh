#!/bin/bash
scp -i ~/.ssh/daniel-IAM-keypair.pem ./producer/sequential_producer.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./producer/s3_producer.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/
#scp -i ~/.ssh/daniel-IAM-keypair.pem ./consumer/fake_consumer.py ubuntu@
scp -i ~/.ssh/daniel-IAM-keypair.pem ./spark/sequential_consumer.py ubuntu@ec2-34-223-204-251.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./spark/start_consumer.sh ubuntu@ec2-34-223-204-251.us-west-2.compute.amazonaws.com:~/
echo "upload complete"
