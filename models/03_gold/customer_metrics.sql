-- models/gold/customer_metrics.sql
select
  customer_id,
  count(*) as orders_count,
  sum(total_amount) as total_spend
from {{ ref('stg_orders') }}
group by customer_id
