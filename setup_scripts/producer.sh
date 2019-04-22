#!/bin/bash
ssh -t -i ~/.ssh/daniel-IAM-keypair.pem ubuntu@${PRODUCER_IP} 'sudo apt update; sudo apt install python3-pip python-pip python3-dev build-essential autoconf libtool; pip3 install smart_open; pip install paramiko; pip3 install kafka-python'
