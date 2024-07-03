use assign;

select * from customer_profile;

select * from product_category_map;

select count(txn_id) from rw_transaction_data;

create table combined_rtd_pcm as
	select * from product_category_map
	inner join  rw_transaction_data using(module_id,product_id,product_type_id);
-- on product_category_map.module_id = rw_transaction_data.module_id
-- and product_category_map.product_id = rw_transaction_data.product_id
-- and product_category_map.product_type_id = rw_transaction_data.product_type_id;
SET SQL_SAFE_UPDATES = 0;

select * from combined_rtd_pcm;

alter table combined_rtd_pcm add column Months int;

update combined_rtd_pcm
set Months = month(last_modified_date);

select count(*) from combined_rtd_pcm;

drop table joinedtc;

create table joinedtc as
select payer_account_id,Months,
SUM(if (txn_flow = 'OutFlow' , amount , 0))AS txn_flow_Ofsum,
SUM(if(txn_flow = 'Value Chain',amount,0))AS txn_flow_VCsum,
SUM(if(txn_flow = 'InFlow',amount, 0 )) AS txn_flow_IFsum,
Count(if (txn_flow = 'OutFlow' , amount , null))AS txn_flow_Ofcount,
Count(if(txn_flow = 'Value Chain',amount,null))AS txn_flow_VCcount,
Count(if(txn_flow = 'InFlow',amount, null )) AS txn_flow_IFcount
from 
combined_rtd_pcm
group by payer_account_id,Months;

drop table joinedtotal_count;

create temporary
table joinedtotal_count as
select payer_account_id,
SUM(if (txn_flow = 'OutFlow' , amount , 0))AS txn_flow_Ofsum,
SUM(if(txn_flow = 'Value Chain',amount,0))AS txn_flow_VCsum,
SUM(if(txn_flow = 'InFlow',amount, 0 )) AS txn_flow_IFsum,
SUM(if (txn_flow = 'OutFlow' AND amount IS NOT NULL,1 ,0 ) )AS txn_OutFlowCount,
SUM(if (txn_flow = 'Value Chain' AND amount IS NOT NULL , 1 ,0 ) )AS txn_ValueChain,
SUM(if (txn_flow = 'InFlow' AND amount IS NOT NULL ,1,0 ) )AS txn_Inflow
from 
combined_rtd_pcm
group by payer_account_id;

select * from joinedtotal_count;

select * from joinedtc;

drop table txn;
create table txn as
select payer_account_id,
sum(txn_flow_Ofsum)AS txn_flow_Of_sum,
sum(txn_flow_VCsum)AS txn_flow_VC_sum,
sum(txn_flow_IFsum)AS txn_flow_IF_sum,
avg(txn_flow_Ofsum)AS txn_flow_Of_avg,
avg(txn_flow_VCsum)AS txn_flow_VC_avg,
avg(txn_flow_IFsum)AS txn_flow_IF_avg,
sum(txn_flow_Ofcount)AS txn_flow_Of_count_s,
sum(txn_flow_VCcount)AS txn_flow_VC_count_s,
sum(txn_flow_IFcount)AS txn_flow_IF_count_s,
avg(txn_flow_Ofcount)AS txn_flow_Of_count_a,
avg(txn_flow_VCcount)AS txn_flow_VC_count_a,
avg(txn_flow_IFcount)AS txn_flow_IF_count_a
from joinedtc
group by payer_account_id;

select * from txn;

select * from combined_rtd_pcm;

alter table combined_rtd_pcm add column last_modified_date_time datetime;

update combined_rtd_pcm set last_modified_date_time =  cast(last_modified_date as datetime) + cast(time as time);

describe combined_rtd_pcm;

select * from combined_rtd_pcm;

-- latest_product
drop table lastest_prod;
create table lastest_prod as
(select payer_account_id, product_name as latest_product_used,last_modified_date_time as latest_transaction_date from
    (SELECT payer_account_id, product_name, last_modified_date_time ,
           ROW_NUMBER() OVER (PARTITION BY payer_account_id ORDER BY last_modified_date_time  DESC) AS rn
    FROM combined_rtd_pcm) ng
where rn =1);
-- select * from joinedtc;
-- select * from lastest_prod;

-- most_used, 2nd_most_used, 3rd_most_used

drop table most_used_pr;
create table most_used_pr as
select payer_account_id,product_name,cnt from(
select payer_account_id ,product_name,
count(product_name) over(partition by payer_account_id,product_name) as cnt
 from combined_rtd_pcm) sub
group by payer_account_id,product_name order by payer_account_id desc,cnt desc;

select * from most_used_pr;

select * ,row_number() over(partition by payer_account_id order by cnt desc) as row_num from most_used_pr;

drop table most_used_product;
create table most_used_product as
select payer_account_id,product_name as most_used_product from most_used_prod where row_num=1;

drop table second_used_product;
create table second_used_product as
select payer_account_id,product_name as second_most_used_prod from most_used_prod where row_num=2;

drop table third_used_product;
create table third_used_product as
select payer_account_id,product_name as third_most_used_prod from most_used_prod where row_num=3;

with cte1 as 
(select payer_account_id,product_name as most_used_product from most_used_prod where row_num=1),

cte2 as (select payer_account_id,product_name as second_most_used_prod from most_used_prod where row_num=2)

select * from cte1 a
inner join cte2 b
on a.payer_account_id = b.payer_account_id;

select * from combined_rtd_pcm;

-- total and monthly_revenue_amt
drop table total_monthly_rev_amt;
create table total_monthly_rev_amt as
select payer_account_id,sum(rev_amt) as total_revenue_amt,avg(rev_amt) as monthly_revenue_amt from(
select payer_account_id,Months,
sum(revenue_amount) as rev_amt from combined_rtd_pcm
group by payer_account_id,Months) sub 
group by payer_account_id;

drop table total_reward_point;
create table total_reward_point as
select payer_account_id, 
	   sum(reward_point) as reward_points
	   from combined_rtd_pcm
       group by payer_account_id;

drop table product_usage;
create table product_usage as
select payer_account_id,count(product_id) as product_usage from combined_rtd_pcm group by payer_account_id;


select * from txn;
select * from lastest_prod;
select * from most_used_product;
select * from second_used_product;
select * from third_used_product;
select * from total_monthly_rev_amt;
select * from total_reward_point;
select * from product_usage;

drop table final_table;
create table final_table as
select * from txn left join lastest_prod using (payer_account_id)
left join most_used_product using (payer_account_id)
left join second_used_product using (payer_account_id)
left join third_used_product using (payer_account_id)
left join total_monthly_rev_amt using (payer_account_id)
left join total_reward_point using (payer_account_id)
left join product_usage using (payer_account_id);

select * from final;