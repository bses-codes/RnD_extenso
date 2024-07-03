# Airflow DAG for Checking Disk Space and Dumping MySQL Table

This repository contains an Apache Airflow DAG (`dag_space.py`) designed to manage disk space requirements before performing a database dump of a MySQL table. The process involves estimating the size of a specified table and verifying sufficient disk space before the dump operation is executed.

## Overview

The DAG consists of several tasks:
1. **Estimate the Size of the Table**: Calculates the estimated size of the MySQL table.
2. **Check Disk Space**: Retrieves available disk space and checks if it is sufficient for the dump operation.
3. **Dump Table**: Dumps the MySQL table to a SQL file if there is sufficient disk space.

## Prerequisites

- Apache Airflow 2.0+
- MySQL server access
- Python 3.6+

## Configuration
Before running the DAG, ensure the MySQL connection (mysql_local) is configured in Airflow's Connections:

Conn Id: mysql_local
Conn Type: MySQL
Host: MySQL server IP or hostname
Schema: Database name
Login: Username
Password: Password

## Task Details
Task Details
- **dump_table**: Executes a shell command to dump the fc_account_master table from the MySQL database.
- **get_space**: Checks the available disk space using a Bash command.
- **check_space**: A Python function that compares the estimated table size with available disk space and raises an error if there is insufficient space.
