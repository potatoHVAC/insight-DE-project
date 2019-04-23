## Running instructions for Olórin demo

* Use 'ssh_scripts/spark_master.sh' to access the spark master node.
* Start Spark Streaming using 'redis_start_consumer.sh' found on the spark master node.
* Use ‘ssh_scripts/producer.sh’ to access the producer node.
* Start ‘friendly_producer.py’ found on the producer node.
* Start ‘src/view_visualizer.sh’ to view input and output traffic in Logstalgia. Note, the windows will open on top of each other.
* Start ‘src/ip_log.sh’ in its own terminal for viewing flagged IP addresses. Note, this will remain blank until the next step.
* Start ‘ddos_producer.py’ found on the producer node to initiate simulated DDOS attack. 