# Transaction Data Analysis 

This repository contains code for analyzing transaction data using Python and various libraries like pandas, matplotlib, seaborn, and MySQL Connector.

## Prerequisites
- Python 3.x
- MySQL database with the necessary tables (`rw_transaction_data`, `product_category_map`, `product_category`, `customer_profile`, `products`)

## Usage

The code performs the following analyses:
   - Data retrieval from MySQL database tables.
   - Data cleaning and preprocessing.
   - Exploratory data analysis (EDA) using box plots and count plots.
   - Aggregation of transaction data based on various parameters.
   - Calculation of summary statistics such as total amounts, counts, averages, etc.
   - Identification of top products and their usage.

### Airflow DAG for Data Analysis

The analysis can be performed using an Airflow DAG, which connects to a MySQL database, retrieves and processes data, and creates a Customer Profile.

The results are presented as dataframes and visualizations within the notebook.

## Results
The Customer profile provides insights into transaction patterns, customer behavior, product usage, and revenue trends based on the provided transaction data.



