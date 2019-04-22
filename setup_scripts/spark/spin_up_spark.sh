#!/bin/bash
#peg up master.yml 
#peg up workers.yml
#peg fetch spark-cluster
#peg sshcmd-cluster spark-cluster "sudo apt install bc"
#peg install spark-cluster ssh
#peg install spark-cluster aws
#peg install spark-cluster environment
#peg install spark-cluster hadoop
#peg service spark-cluster hadoop start
#peg install spark-cluster spark
#peg service spark-cluster spark start
peg sshcmd-cluster spark-cluster "sudo apt update -y; sudo apt install libpq-dev -y;"
peg sshcmd-cluster spark-cluster "pip install redis"
peg sshcmd-cluster spark-cluster "pip install pyspark"
peg sshcmd-cluster spark-cluster "pip install kafka-python"
