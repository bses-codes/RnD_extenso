use client_rw;

create database fc_facts;
-- LOAD DATA LOCAL INFILE '/Users/bses/F1_Intern/assignment_2/fc_account_master.csv' 
-- INTO TABLE fc_account_master
-- FIELDS TERMINATED BY ',' 
-- ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
-- IGNORE 1 ROWS (account_number,customer_code,product,product_category,acc_open_date,acc_closed_date,active_flag);

Select * from fc_account_master;


create table fc_transaction_base(
tran_date text,
account_number text,
branch text,
product text,
lcy_amount text,
transaction_code text,
description1 text,
dc_indicator text,
is_salary text);

-- LOAD DATA LOCAL INFILE '/Users/bses/F1_Intern/assignment_2/fc_transaction_base.csv' 
-- INTO TABLE fc_transaction_base
-- FIELDS TERMINATED BY ',' 
-- ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
-- IGNORE 1 ROWS (tran_date,account_number,branch,product,lcy_amount,transaction_code,description1,dc_indicator,is_salary);

Select * from fc_transaction_base;

CREATE TABLE fc_deposit_facts AS
SELECT account_number,customer_code, sum(case when average_dep <> 0 or average_with <>0 then 1 else 0 end) as frequency, 
avg(average_dep) as overall_avg_dep, 
avg(average_with) as overall_avg_with,
avg(std_dep) as overall_std_dep, 
avg(std_with) as overall_std_with,
avg(var_dep) as overall_var_dep, 
avg(var_with) as overall_var__with 
INTO OUTFILE 'data.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
from(
Select tb.account_number,customer_code,month(tran_date),
avg(case when dc_indicator = 'deposit' then lcy_amount end) as average_dep,
std(case when dc_indicator = 'deposit' then lcy_amount end) as std_dep,
variance(case when dc_indicator = 'deposit' then lcy_amount end) as var_dep,
avg(case when dc_indicator = 'withdraw' then lcy_amount end) as average_with,
std(case when dc_indicator = 'withdraw' then lcy_amount end) as std_with,
variance(case when dc_indicator = 'withdraw' then lcy_amount end) as var_with
from fc_transaction_base as tb JOIN fc_account_master as am on tb.account_number = am.account_number
group by tb.account_number, customer_code, month(tran_date)) as monthly_data 
group by account_number, customer_code;


select * from t_table;