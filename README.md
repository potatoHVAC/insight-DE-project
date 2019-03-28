# ZooKeeper’s Missing Menagerie

By Daniel Speer

A project for the Insight Data Engineering Fellowship.

# Introduction

[There is a bug in Kafka](https://issues.apache.org/jira/browse/KAFKA-7122) where data can be lost when the lead Kafka broker times out from ZooKeeper. This error occurs because the lead broker will continue to accept writes from the producer in the few seconds between disconnecting from ZooKeeper and realizing that it has timed out. This leads to an incorrect offset on that node that can be introduced into the cluster when the node eventually recovers and takes over as the lead broker again. 

# Tech Stack

1. S3
2. Boto
3. Kafka
4. Spark
5. Postgres
6. Flask

# Data Source

Reddit user comments
* [Information](https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/)
* [Torrent](https://mega.nz/#!ysBWXRqK!yPXLr25PgJi184pbJU3GtnqUY4wG7YvuPpxJjEmnb9A)

# Engineering Challenge

* Reproduce the error by artificially disconnection the lead broker from ZooKeeper.
* Isolating the root cause of the error.
* Logging the data loss event only if it happened (not every timeout loses data).

# Business Value

The only thing more damaging than losing data is not knowing that it was even lost. Kafka is a widely used message broker for handling big data sets and though they claim to have exactly-once processing there are a few cracks in the system where data can be lost. My project focuses on one of those holes in an effort to help bring Kafka closer to their goal.

# MVP

Reliably reproduce the bug and create a log entry alerting the user to lost data packets.

# Stretch Goals

* Automatically recover from the lead broker’s timeout without data loss.
