#!/bin/bash

# producer 
scp -i ~/.ssh/daniel-IAM-keypair.pem ./variable_library.py ubuntu@ec2-35-165-94-127.us-west-2.compute.amazonaws.com:~/

# kafka

# spark
scp -i ~/.ssh/daniel-IAM-keypair.pem ./variable_library.py ubuntu@ec2-35-165-101-226.us-west-2.compute.amazonaws.com:~/

# postgresql

# dash

scp -i ~/.ssh/daniel-IAM-keypair.pem ./variable_library.py ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com:~/