#!/bin/bash
(ssh -i ~/.ssh/daniel-IAM-keypair.pem ubuntu@${VISUALIZER_IP} ./input_consumer.py | logstalgia --hide-response-code --speed 2 --disable-glow --title 'Raw Input' -) &
(ssh -i ~/.ssh/daniel-IAM-keypair.pem ubuntu@${VISUALIZER_IP} ./output_consumer.py | logstalgia --hide-response-code --speed 2 --disable-glow --title 'Olorin' -) &
