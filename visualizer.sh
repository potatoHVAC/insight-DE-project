#!/bin/bash
(ssh -i ~/.ssh/daniel-IAM-keypair.pem ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com ./input_consumer.py | logstalgia -s 10 --hide-response-code --title 'Raw Input' -) &
(ssh -i ~/.ssh/daniel-IAM-keypair.pem ubuntu@ec2-34-218-254-7.us-west-2.compute.amazonaws.com ./output_consumer.py | logstalgia -s 10 --hide-response-code --title 'Olorin' -) &
