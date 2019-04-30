# Running instructions for Olórin demo


* SSH into Spark master node.
```bash
$ ./ssh_scripts/spark_master.sh
```
* Start Spark Streaming.
```bash
sparkeMasterNode: $ ./redis_start_consumer.sh
```
* SSH into producer node.
```bash
$ ./ssh_scripts/producer.sh
```
* Start the friendly producer.
```bash
producerNode: $ ./friendly_producer.py
```
* Start the Logstalgia visualizer
```bash
$ ./src/view_visualizer.sh
```
Note: the windows will open on top of each other and will not open until messages have been passed into Olórin.
* Start the ip log to view flagged IPs in real time on the command line.
```bash
$ ./src/ip_log.sh
```
* Start and stop friendly or DDOS traffic on the producer node.
```bash
producerNode: $ ./friendly_producer.py
producerNode: $ ./ddos_producer.py
```