#!/bin/bash
spark-submit --master spark://ec2-35-165-101-226.us-west-2.compute.amazonaws.com:7077 --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.1 ./consumer.py
