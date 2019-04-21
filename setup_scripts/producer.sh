#!/bin/bash
ssh -t -i ~/.ssh/daniel-IAM-keypair.pem ubuntu@${PRODUCER_IP} 'sudo apt update; sudo apt install python3-pip; pip3 install smart_open; pip3 install paramiko;'
