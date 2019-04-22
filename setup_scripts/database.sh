#!/bin/bash
ssh -t -i ~/.ssh/daniel-IAM-keypair.pem ubuntu@${DATABASE_IP} 'sudo apt update; sudo apt install redis-server;'
