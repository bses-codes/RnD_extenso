# Time Series Analysis of Stock Indices

This repository contains Python code that performs comprehensive time series analysis on historical stock index data. The analysis includes visualization, statistical testing, and modeling of stock indices like SPX and FTSE using ARIMA and other statistical models.

## Overview of Scripts

The script processes data from CSV files, visualizes time series data, performs statistical tests to check for stationarity, decomposes series into seasonal components, and fits ARIMA models to understand dependencies and predict future values.

## Features

- **Data Visualization**: Visualizes the historical trends of various stock indices.
- **Statistical Testing**: Includes tests like the Augmented Dickey-Fuller test to determine the stationarity of a series.
- **Seasonal Decomposition**: Analyzes the seasonal aspects of the indices.
- **AutoCorrelation and Partial AutoCorrelation**: Visual analysis to identify autocorrelation in data.
- **ARIMA Modeling**: Application of ARIMA models to forecast future values based on historical data.
- **Random Walk and White Noise Visualization**: Compares the stock indices against random walk and white noise models.

## Dependencies

- Python 3.6+
- NumPy
- pandas
- matplotlib
- seaborn
- statsmodels
- scipy
