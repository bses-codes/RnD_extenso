# Kafka Spark Data Encryption and Decryption

This project demonstrates how to produce and consume data with encryption and decryption using Apache Kafka and Apache Spark.

## Introduction

The project consists of several components:

- **Producer Encryption (`producer_enc.ipynb`)**: This notebook contains code for producing data with encryption. It encrypts sensitive data (e.g., account numbers) using AES encryption before sending it to Kafka.

- **Consumer Decryption (`consumer_dec.ipynb`)**: This notebook contains code for consuming encrypted data from Kafka and decrypting it using the appropriate encryption key.

- **Consumer (`consumer.ipynb`)**: This notebook demonstrates reading data produced by two producers.


## Notebooks

### Producer Encryption (`producer_enc.ipynb`)

This notebook demonstrates how to:

- Produce data with encryption using AES encryption.
- Send encrypted data to Kafka topic for consumption.

### Consumer Decryption (`consumer_dec.ipynb`)

This notebook demonstrates how to:

- Consume encrypted data from Kafka topic.
- Decrypt encrypted data using the appropriate encryption key.

### Consumer (`consumer.ipynb`)

This notebook demonstrates:

- Reading data produced by two producers.

## Requirements

- Apache Kafka
- Apache Spark
- Python 3.x
- PySpark
- Kafka-python
- Fernet

## Usage

1. Install MySQL and kafka on the host machine. 
2. Excute the following commands in terminal: `<location to kafka/bin folder>/zookeeper-server-start.sh <location to kafka/config folder>/zookeeper.properties` and `<location to kafka/bin folder>/kafka-server-start.sh <location to kafka/config folder>/server.properties`
4. Run the Producer notebook (`producer.ipynb`) to produce data and send it through specified topic.
5. Run the Consumer notebook (`consumer.ipynb`) to consume the sent data.

