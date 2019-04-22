#!/bin/bash
spark-submit --master spark://ec2-34-212-188-254.us-west-2.compute.amazonaws.com:7077 --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.1 ./redis_consumer.py
#spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.1 ./redis_consumer.py
