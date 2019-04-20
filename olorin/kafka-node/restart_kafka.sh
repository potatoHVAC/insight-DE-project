#!/bin/bash
peg fetch kafka-cluster
peg service kafka-cluster kafka stop
peg service kafka-cluster zookeeper stop
peg service kafka-cluster zookeeper start
peg service kafka-cluster kafka start
