with bronze_orders as (
    -- We reference the BRONZE model, NOT the raw source
    select * from {{ ref('b_orders') }}
)

select
    -- Rename ugly CSV headers to clean names
    order_id,
    customer_id,
    order_status,
    cast(order_purchase_timestamp as timestamp) as purchased_at,
    cast(order_delivered_customer_date as timestamp) as delivered_at
from bronze_orders
where order_id is not null