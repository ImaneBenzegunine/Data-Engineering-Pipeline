-- models/gold/dim_customers.sql
select
  customer_id,
  first_name,
  last_name,
  email,
  concat(first_name, ' ', last_name) as full_name
from {{ ref('stg_customers') }}
