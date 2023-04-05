select *
from `Online Retail`;


-- Clean Table
-- Create recipient column
ALTER TABLE `Online Retail`
    DROP InvoiceDate_Clean,
    ADD InvoiceDate_Clean date;

-- Apply cleaned data to recipient column
UPDATE `Online Retail`
SET `Online Retail`.InvoiceDate_Clean = STR_TO_DATE(InvoiceDate,'%m/%d/%Y %H:%i');

-- check if cleaned
SELECT max(`Online Retail`.InvoiceDate_Clean)
from `Online Retail`;

-- Update table to reflect cleaned data
ALTER TABLE `Online Retail`
    MODIFY COLUMN InvoiceDate_Clean datetime AFTER InvoiceDate;

-- ALTER TABLE `Online Retail`
--     DROP COLUMN InvoiceDate;

-- ALTER TABLE `Online Retail`
--     RENAME COLUMN Invoice_Date_Clean TO InvoiceDate;

-- Total records: 541909
select count(*)
from `Online Retail`;

-- Check for customers without IDs:
-- 135080 records without IDs
-- 406829 records with IDs
select *
from `Online Retail`
where CustomerID is null;

select count(*)
from `Online Retail`
where CustomerID is null;

select count(*)
from `Online Retail`
where CustomerID is not null;

-- Check for records with negative quantities: 10624
-- These are returned items
select *
from `Online Retail`
where Quantity < 0;

select count(*)
from `Online Retail`
where Quantity < 0;

-- Records with Customer ID, and positive value Unit Price & Quantity
-- 397,884
select *
from `Online Retail`
where CustomerID is not null and Quantity > 0 and UnitPrice > 0;


-- Check for duplicates
-- 387344 Unique data
-- 10041 duplicate data
with id_qty_price as
         (
             select *
             from `Online Retail`
             where CustomerID is not null and Quantity > 0 and UnitPrice > 0
         ), dup_check as
             (
                 select *, count(*) over (partition by InvoiceNo, StockCode, Quantity order by InvoiceDate) as duplicates
                 from id_qty_price i
                 -- where duplicates > 1
                 -- order by duplicates desc
)
select *
from dup_check
where duplicates = 1
;

-- Create temp table of unique data
drop table if exists online_retail_temp;
create temporary table online_retail_temp
with id_qty_price as
         (
             select *
             from `Online Retail`
             where CustomerID is not null and Quantity > 0 and UnitPrice > 0
         ), dup_check as
         (
             select *, count(*) over (partition by InvoiceNo, StockCode, Quantity order by InvoiceDate) as duplicates
             from id_qty_price i
             -- where duplicates > 1
             -- order by duplicates desc
         )
select *
from dup_check
where duplicates = 1
;

select *
from online_retail_temp;

-- Cohort Analysis: To see trends and patterns of behaviour of customers
-- A cohort is a group of people with common characteristics
-- We'll be doing Time-based (Retention) Cohort Analysis to understand LTV
-- Others include size-based and segment-based cohort analysis
-- Required Data points / Labels
-- 1. Unique Identifiers for the group to be analysed, e.g. CustomerID
-- 2. Initial Start Date, e.g. First Invoice Date - to derive cohort group
-- 3. Revenue Data e.g.

drop table if exists cohort_temp;
create temporary table cohort_temp
select CustomerID, min(InvoiceDate_Clean) as first_purchase_date,
       concat(year(min(InvoiceDate_Clean)), '-', date_format(min(InvoiceDate_Clean), '%m'), '-', '01') as cohort_date
       -- concat(year(min(InvoiceDate_Clean)),'-', month(min(InvoiceDate_Clean)),'-', '01') as cohort_date
from online_retail_temp
group by CustomerID;


select *
from cohort_temp;

select distinct cohort_date
from cohort_temp;

select distinct date_format(InvoiceDate_Clean, '%m')
from `Online Retail`;

-- Create cohort index
-- This is an integer representation of the number of months
-- that have passed since the customer's first engagement/ purchase
drop table if exists  cohort_retention_temp;
create temporary  table cohort_retention_temp
select o3.*, -- 3rd stage: Calc the index
       -- year_diff * 12 + month_diff as cohort_index
       year_diff * 12 + month_diff + 1 as cohort_index

from (select o2.*, -- 2nd stage: calc diff between year & month for invoice & cohort
             invoice_year - cohort_year   as year_diff,
             invoice_month - cohort_month as month_diff
      from (select o.*, -- 1st stage: find cohort year/month and invoice year/month
                   c.cohort_date,
                   year(o.InvoiceDate_Clean)          as invoice_year,
                   month(o.InvoiceDate_Clean)         as invoice_month,
                   year(cast(c.cohort_date as date))  as cohort_year,
                   month(cast(c.cohort_date as date)) as cohort_month
            from online_retail_temp o
                     left join cohort_temp c
                               on o.CustomerID = c.CustomerID) as o2
      ) as o3
;

select *
from cohort_retention_temp;

select distinct CustomerID, cohort_date, cohort_index
from cohort_retention_temp
order by CustomerID, cohort_index;

select distinct cohort_index
from cohort_retention_temp;

-- Pivot Data to see the Cohort Table
create temporary  table  cohort_pivot_temp
SELECT cohort_date,
       count(distinct(case when cohort_index = 1 then CustomerID else null end)) as '1',
       count(distinct(case when cohort_index = 2 then CustomerID else null end)) as '2',
       count(distinct(case when cohort_index = 3 then CustomerID else null end)) as '3',
       count(distinct(case when cohort_index = 4 then CustomerID else null end)) as '4',
       count(distinct(case when cohort_index = 5 then CustomerID else null end)) as '5',
       count(distinct(case when cohort_index = 6 then CustomerID else null end)) as '6',
       count(distinct(case when cohort_index = 7 then CustomerID else null end)) as '7',
       count(distinct(case when cohort_index = 8 then CustomerID else null end)) as '8',
       count(distinct(case when cohort_index = 9 then CustomerID else null end)) as '9',
       count(distinct(case when cohort_index = 10 then CustomerID else null end)) as '10',
       count(distinct(case when cohort_index = 11 then CustomerID else null end)) as '11',
       count(distinct(case when cohort_index = 12 then CustomerID else null end)) as '12',
       count(distinct(case when cohort_index = 13 then CustomerID else null end)) as '13'
FROM cohort_retention_temp
GROUP BY cohort_date;

-- Create cohort retention rate
-- Divide each cohort section by cohort 1
select cohort_date,
       COUNT(distinct(CASE WHEN cohort_index = 1 THEN CustomerID END)) * 100.0 / COUNT(distinct(CASE WHEN cohort_index = 1 THEN CustomerID END)) AS '1',
       COUNT(distinct(CASE WHEN cohort_index = 2 THEN CustomerID END)) * 100.0 / COUNT(distinct(CASE WHEN cohort_index = 1 THEN CustomerID END)) AS '2',
       COUNT(distinct(CASE WHEN cohort_index = 3 THEN CustomerID END)) * 100.0 / COUNT(distinct(CASE WHEN cohort_index = 1 THEN CustomerID END)) AS '3',
       COUNT(distinct(CASE WHEN cohort_index = 4 THEN CustomerID END)) * 100.0 / COUNT(distinct(CASE WHEN cohort_index = 1 THEN CustomerID END)) AS '4',
       COUNT(distinct(CASE WHEN cohort_index = 5 THEN CustomerID END)) * 100.0 / COUNT(distinct(CASE WHEN cohort_index = 1 THEN CustomerID END)) AS '5',
       COUNT(distinct(CASE WHEN cohort_index = 6 THEN CustomerID END)) * 100.0 / COUNT(distinct(CASE WHEN cohort_index = 1 THEN CustomerID END)) AS '6',
       COUNT(distinct(CASE WHEN cohort_index = 7 THEN CustomerID END)) * 100.0 / COUNT(distinct(CASE WHEN cohort_index = 1 THEN CustomerID END)) AS '7',
       COUNT(distinct(CASE WHEN cohort_index = 8 THEN CustomerID END)) * 100.0 / COUNT(distinct(CASE WHEN cohort_index = 1 THEN CustomerID END)) AS '8',
       COUNT(distinct(CASE WHEN cohort_index = 9 THEN CustomerID END)) * 100.0 / COUNT(distinct(CASE WHEN cohort_index = 1 THEN CustomerID END)) AS '9',
       COUNT(distinct(CASE WHEN cohort_index = 10 THEN CustomerID END)) * 100.0 / COUNT(distinct(CASE WHEN cohort_index = 1 THEN CustomerID END)) AS '10',
       COUNT(distinct(CASE WHEN cohort_index = 11 THEN CustomerID END)) * 100.0 / COUNT(distinct(CASE WHEN cohort_index = 1 THEN CustomerID END)) AS '11',
       COUNT(distinct(CASE WHEN cohort_index = 12 THEN CustomerID END)) * 100.0 / COUNT(distinct(CASE WHEN cohort_index = 1 THEN CustomerID END)) AS '12',
       COUNT(distinct(CASE WHEN cohort_index = 13 THEN CustomerID END)) * 100.0 / COUNT(distinct(CASE WHEN cohort_index = 1 THEN CustomerID END)) AS '13'
from cohort_retention_temp
group by cohort_date;

