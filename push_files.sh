#!/bin/bash
scp -i ~/.ssh/daniel-IAM-keypair.pem ./producer/sequential_producer.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/
scp -i ~/.ssh/daniel-IAM-keypair.pem ./consumer/fake_consumer.py ubuntu@ec2-35-160-177-132.us-west-2.compute.amazonaws.com:~/
echo "upload complete"
