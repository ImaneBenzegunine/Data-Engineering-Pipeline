with bronze_customers as (
    -- We reference the BRONZE model, NOT the raw source
    select * from {{ ref('b_customers') }}
)

select
    -- Rename ugly CSV headers to clean names
    customer_id,
    customer_unique_id,
    customer_city,
    customer_state
from bronze_customers
where customer_id is not null