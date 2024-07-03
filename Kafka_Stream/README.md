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

1. Run the Producer Encryption notebook (`producer_enc.ipynb`) to produce encrypted data.
2. Run the Consumer Decryption notebook (`consumer_dec.ipynb`) to consume and decrypt the encrypted data.
3. Run the Consumer notebook (`consumer.ipynb`), adjust the variables after running any two producers to read data from both producers.
