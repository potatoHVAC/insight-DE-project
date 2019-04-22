#!/bin/bash
ssh -t -i ~/.ssh/daniel-IAM-keypair.pem ubuntu@${VISUALIZER_IP} 'sudo apt update; sudo apt install python3-pip libpq-dev; pip3 install kafka-python;'
