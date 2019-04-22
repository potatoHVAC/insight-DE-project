#!/bin/bash
#peg up master.yml
#peg up workers.yml
#peg fetch kafka-cluster
#peg sshcmd-cluster kafka-cluster "sudo apt upgrade -y; sudo apt install bc -y;"
peg install kafka-cluster ssh
peg install kafka-cluster aws
peg install kafka-cluster environment
peg install kafka-cluster zookeeper
peg service kafka-cluster zookeeper start
peg install kafka-cluster kafka
peg service kafka-cluster kafka start
