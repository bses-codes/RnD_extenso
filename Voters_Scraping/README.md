# Web Scraping for Voter List Data

This repository contains a Python script that automates the extraction of voter list data from a specified URL using Selenium and BeautifulSoup. The script navigates through multiple dropdowns, submits forms, and collects data from dynamically generated tables.

## Overview

The script uses the Selenium WebDriver to interact with the web page, handle dropdown selections, submit forms, and navigate through paginated data. BeautifulSoup is used to parse HTML and extract data from tables. Data from each page is collected into a pandas DataFrame, which can be used for further analysis or saved to a file.

## Features

- **Automated Browser Interaction**: Uses Selenium to simulate user interactions like selecting dropdown options and clicking buttons.
- **Data Extraction**: Utilizes BeautifulSoup to parse HTML and extract table data.
- **Pagination Handling**: Automatically navigates through paginated data.
- **Data Aggregation**: Aggregates all data into a single pandas DataFrame.

## Requirements

To run this script, you will need the following:
- Python 3.6 or higher
- Selenium
- BeautifulSoup4
- pandas

## Usage
- Ensure all dependencies are installed and the WebDriver is set up correctly.
- Modify the script to target specific dropdown indices or adjust other parameters as needed.
- Run the script.
- The script will open a browser window, navigate through the site, and collect data into a DataFrame.

## Configuration

- **Dropdown Navigation**: The script is configured to loop through specified ranges for state, district, municipality, ward, and registration center dropdowns. Adjust these ranges based on the required data extraction scope.
- **Timeouts**: Adjust WebDriverWait timeouts based on your network speed and the response time of the website.

## Outputs
The data collected by the script is stored in a pandas DataFrame, which can be exported to CSV or another format as required.
