# Olórin

<div style="text-align:center; margin: 50px 0"><img src ="/images/olorin_logo.png" height="150"/></div>

By Daniel Speer

A project for the Insight Data Engineering Fellowship.

[Presentation slides](http://bit.ly/2Xh1gkm)

<hr/>

## Setup Instructions

#### Install support software

* Install [Pegasus](https://github.com/InsightDataScience/pegasus)
* Install [Logstalgia](https://logstalgia.io/#)

#### Spin up EC2 Instances

* Create a VPC and security group in AWS for this project.
* Edit the master.yml and worker.yml files located in `setup_scripts/kafka/*.yml` and `setup_scripts/spark/*.yml` replacing the subnet_id and security_group_id with your own from the previous step.
* Spin up kafka-cluster.
```bash
$ setup_scripts/kafka/spin_up_kafka.sh
```
* Spin up spark-cluster.
```bash
$ setup_scripts/spark/spin_up_spark.sh
```
* Initialize three more EC2 instances with public IP addresses and label them producer, database, and visualizer.

#### Setup environment

* Add the following lines to your `~/.bash_profile`
```bash
export OLORIN_HOME=<insert path to Olorin Directory>
export KAFKA_MASTER_IP=<insert IP>
export SPARK_MASTER_IP=<insert IP>
export PRODUCER_IP=<insert IP>
export DATABASE_IP=<insert IP>
export VISUALIZER_IP=<insert IP>
```
* Source the `.bash_profile` when finished.
```bash
$ source ~/.bash_profile
```
* Update the IP address in `olorin/spark/redis_start_consumer.py` to the Spark Master IP.
#### Install the required software on the three support nodes.
```bash
$ ./setup_scripts/producer_setup.sh
$ ./setup_scripts/database_setup.sh
$ ./setup_scripts/visualizer_setup.sh
```
* SSH into producer node.
```bash
$ ./ssh_scripts/producer.sh
```
* Configure AWS credentials on the producer node.
```bash
producerNode: $ aws configure
```
* SSH into database node.
```bash
$ ./ssh_scripts/producer.sh
```
* Update bind ports for Redis in `/etc/redis/redis.conf`
 * Change `bind 127.0.0.1` to `bind 0.0.0.0`
* Restart Redis server.
```bash
databaseNode: $ sudo service redis-server restart
```
* Add `vm.overcommit_memory = 1` to the end of `/etc/sysctl.conf`
 
<hr/>

## Introduction

## Architecture

* Python Producer
* Kafka
* Spark Streaming
* Redis

## Engineering Challenges


