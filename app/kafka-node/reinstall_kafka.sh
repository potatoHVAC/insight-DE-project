#!/bin/bash
peg fetch kafka-cluster
peg uninstall kafka-cluster kafka
peg uninstall kafka-cluster zookeeper
peg install kafka-cluster zookeeper
peg service kafka-cluster zookeeper start
peg install kafka-cluster kafka
peg service kafka-cluster kafka start
