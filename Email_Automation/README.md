# Automated Email Sending DAG

This repository contains an Apache Airflow DAG, `first_dag`, designed specifically for sending scheduled emails. The DAG is configured to send an email at a specified time.

## Overview

The DAG `first_dag` is set up to execute a single task that sends an email at 04:25 AM every day. This setup demonstrates the basic usage of the `EmailOperator` in Airflow to automate the process of sending emails.

## Prerequisites

To run this DAG, you need:
- Apache Airflow 2.0+
- SMTP server access for sending emails

## Configuration
You must configure Airflow to use an SMTP server for sending emails. This is done in the Airflow configuration file (airflow.cfg):

- smtp_host: Your SMTP server address.
- smtp_starttls: Set to True to enable TLS (recommended).
- smtp_ssl: Set to False unless your SMTP server requires SSL directly.
- smtp_user: Your SMTP username.
- smtp_password: Your SMTP password.
- smtp_port: SMTP server port (commonly 587 for TLS).
- smtp_mail_from: Email address used as the sender.

## Task Details
- **send_email**: Uses the EmailOperator to send an email. The recipient, subject, and content of the email are defined within the task.
