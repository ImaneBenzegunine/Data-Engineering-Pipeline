import os
from pyspark.sql import SparkSession

# 1. Setup Spark to download the Postgres Translator (JDBC)
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.postgresql:postgresql:42.7.3 pyspark-shell'

spark = SparkSession.builder \
    .appName("OlistIngestion") \
    .getOrCreate()

# 2. Connection Settings
# Use 'postgres' (the service name in docker-compose), NOT localhost
db_url = "jdbc:postgresql://postgres:5432/data_warehouse" 
db_properties = {
    "user": "postgres",
    "password": "root", 
    "driver": "org.postgresql.Driver"
}

# 3. Path INSIDE the container (mapped in docker-compose)
data_path = "/opt/airflow/data/raw"

def ingest_data():
    # List of files in your kaggle/data/raw folder
    files = {
        "olist_orders_dataset.csv": "orders",
        "olist_customers_dataset.csv": "customers",
        "olist_order_items_dataset.csv": "order_items",
        "olist_products_dataset.csv": "products"
    }

    for file_name, table_name in files.items():
        full_path = os.path.join(data_path, file_name)
        
        if os.path.exists(full_path):
            print(f"--- Reading {file_name} ---")
            # Spark reads the CSV
            df = spark.read.csv(full_path, header=True, inferSchema=True)
            
            # Spark writes to the 'raw' schema in Postgres
            print(f"--- Writing to raw.{table_name} ---")
            df.write.jdbc(url=db_url, table=f"raw.{table_name}", mode="overwrite", properties=db_properties)
        else:
            print(f"❌ File not found: {full_path}")

if __name__ == "__main__":
    ingest_data()
    spark.stop()