# Customer Transaction Analysis: RFM Segmentation

This repository contains a Python script that analyzes customer transaction data using the RFM (Recency, Frequency, Monetary) model. 
The datasets contains the following columns: tran_date,account_number,branch,product,lcy_amount,transaction_code,description1,dc_indicator,is_salary.
## Overview

The script reads transaction data from a CSV file, processes the data to extract RFM metrics, and then segments the customers into different groups based on these metrics. The groups are visualized using histograms and a treemap to provide insights into customer behavior patterns.

## Features

- **Recency**: Calculates how recently a customer has made a transaction.
- **Frequency**: Calculates how often a customer makes transactions.
- **Monetary**: Calculates the total amount of money a customer has spent.
- **RFM Segmentation**: Segments customers based on recency, frequency, and monetary values.
- **Visualization**: Provides histograms of RFM metrics and a treemap of customer segments.

## Requirements

To run this script, you will need the following libraries:
- Pandas
- Matplotlib
- Seaborn
- Squarify

## Visualization Outputs

The script will generate the following plots:
- **Histograms** for Recency, Frequency, and Monetary values.
- **Treemap** for visualizing the distribution of RFM segments.

## RFM Analysis Results

Results of the RFM analysis including segmentation labels such as Premium, Loyal, Potential, Promising, and Needs Attention are stored in a dataframe and printed to the console.
