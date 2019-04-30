# Olórin

<div style="text-align:center; margin: 50px 0"><img src ="/images/olorin_logo.png" height="150"/></div>

By Daniel Speer

A project for the Insight Data Engineering Fellowship.

[Presentation slides](http://bit.ly/2Xh1gkm)

<hr/>

## Introduction

Olórin is a real time apache log monitoring system for identifying high volume users. 

<hr/>

## Setup Instructions

#### Install local support software

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

## Architecture

<div style="text-align:center; margin: 50px 0"><img src ="/images/Olorin.png" height="500"/></div>

## Engineering Challenges

Originally Olórin used PostgreSLQ to view all connections for a given ip over a set window of time. This resulted in an unnecessary amount of archived data and long check times for each connection. Both of these problems prevent  Olórin from being a practical solution for a high volume web server. 

#### Algorithm Switch

The historical log was eliminated by switching to a token system for keeping track of IP activity. Each IP is given an initial set of tokens representing an allowed transaction. Olórin will now store a single entry per IP with a time stamp for their last interaction and their remaining tokens. Every transaction going forward will compare the current time to their last interaction and update their token count accordingly – up to a maximum value – before reducing their token count by one. This reduces the stored data from an extensive record of all transactions to a single entry per IP address. 

#### Database Selection

Updating the algorithm for identifying high volume IP addresses changed the required behavior of the database.  Olórin no longer requires relational checks but instead is using a key value store with at most two connections per Apache log so Redis was selected for its fast reads and writes functionality. 

#### Kafka Improvements

Switching the algorithm and database had over 2X improvements on functionality and no longer slows down as we scale up the number of IP addresses but it still has not reached usable numbers. From here it was identified that Kafka was operating on a single partition. Increasing the partition count to match the number of Spark consumers resulted in a 12X increase in performance. 