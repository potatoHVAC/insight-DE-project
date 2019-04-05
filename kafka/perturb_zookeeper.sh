#!/bin/bash
ps aux | grep "zookeeper" | awk '{print $2}'
sudo kill -9 $(ps aux | grep "zookeeper" | awk '{if(NR==2)print $2}')
zkServer.sh start &
sudo /usr/local/kafka/bin/kafka-server-start.sh /usr/local/kafka/config/server.properties &
ps aux | grep "zookeeper" | awk '{print $2}'
