#!/bin/bash
scp -i ~/.ssh/daniel-IAM-keypair.pem ./producer/sequential_producer.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./producer/s3_producer.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/
#scp -i ~/.ssh/daniel-IAM-keypair.pem ./consumer/fake_consumer.py ubuntu@
scp -i ~/.ssh/daniel-IAM-keypair.pem ./spark/consumer.py ubuntu@ec2-35-165-101-226.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./spark/start_consumer.sh ubuntu@ec2-35-165-101-226.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./kafka/perturb_zookeeper.sh ubuntu@ec2-52-39-96-200.us-west-2.compute.amazonaws.com:~/
echo "upload complete"
