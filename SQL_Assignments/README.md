# SQL Script Repository

This repository contains a set of SQL scripts designed for creating and querying databases as part of an assignment. Each script serves a specific purpose, from setting up databases and tables to querying data based on specific criteria.

## Overview of Scripts

1. **assign1.sql** - This script sets up initial databases and tables, imports data, and creates aggregate views.
2. **Balance.sql** - This script creates a database and performs data transformations to compute running balances.
3. **salary.sql** - This script queries for transactions that include salaries.

## Script Details

### 1. assign1.sql

- **Database Initialization**: Sets the context to `client_rw` and creates a new database `fc_facts`.
- **Table Creation and Data Import**:
  - Creates `fc_account_master` and `fc_transaction_base` tables.
  - Previously, data was loaded from local CSV files. These sections are commented out but can be reactivated if needed.
- **Queries**:
  - The script includes queries to select everything from the tables mentioned above.
- **Aggregation**:
  - Creates `fc_deposit_facts` table by aggregating data from the transaction and account master tables.


### 2. Balance.sql

- **Database and Table Setup**: Creates an `assign` database and sets up a `balance` table based on the `encoded-transaction_summary`.
- **Data Transformation**:
  - Calculates running balances for accounts after cleaning and formatting data fields.
- **Queries**:
  - The script also includes queries to review the data transformations and the final balances computed.

### 3. salary.sql

- **Data Querying**: Selects records from `fc_transaction_base` where transactions are related to salaries.
- **Context Setting**: Uses the `client_rw` database.

