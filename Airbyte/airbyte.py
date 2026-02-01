import airbyte as ab

# Use the "File" source connector via code
source = ab.get_source(
    "source-file",
    config={
        "dataset_name": "olist_data",
        "format": "csv",
        "url": "https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce"
    }
)

# Check connection
source.check()

# Read data and send to a "cache" (like DuckDB or Postgres)
result = source.read()