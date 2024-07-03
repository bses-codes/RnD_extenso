create database assign;
use assign;

select * from `encoded-transaction_summary`;
drop table balance;
Create table balance as
SELECT 
  ROW_NUMBER() OVER(PARTITION by `Account No` ORDER BY DATE) AS RN, REPLACE(`Account No`,"'","") as acc,
  DATE, REPLACE(`WITHDRAWAL AMT`,',','') as WIT, REPLACE(`DEPOSIT AMT`,',','') as DEP
FROM `encoded-transaction_summary`;

select * from balance;

select RN,acc, DATE, WIT, DEP, SUM(DEP-WIT) over (PARTITION by acc ORDER by RN) as bal
from balance;