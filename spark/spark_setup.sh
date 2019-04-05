#!/bin/bash
peg up master.yml
peg up workers.yml
peg fetch spark-cluster
peg install spark-cluster environment
peg install spark-cluster ssh
peg install spark-cluster aws
peg install spark-cluster hadoop
peg service spark-cluster hadoop start
peg install spark-cluster spark
peg service spark-cluster spark start
