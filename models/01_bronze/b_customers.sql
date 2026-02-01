{{ config(materialized='table') }}

with raw_data as (
    select * from {{ source('airbyte_raw', 'olist_customers_dataset') }}
)

select
    *,
    -- Add metadata for engineering traceability
    current_timestamp as dbt_updated_at,
    'kaggle_olist_v1' as data_source_version
from raw_data