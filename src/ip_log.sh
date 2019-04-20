#!/bin/bash
(ssh -i ~/.ssh/daniel-IAM-keypair.pem ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com rm ./producer_logs/ip.log)
(ssh -i ~/.ssh/daniel-IAM-keypair.pem ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com touch ./producer_logs/ip.log)
(ssh -i ~/.ssh/daniel-IAM-keypair.pem ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com ./ip_consumer.py) &
(ssh -i ~/.ssh/daniel-IAM-keypair.pem ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com tail -f ./producer_logs/ip.log)
