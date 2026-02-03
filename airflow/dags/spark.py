from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='olist_pipeline',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    # 1. Create the schema in Postgres
    create_schema = BashOperator(
        task_id='create_schema',
        env={'PGPASSWORD': 'root'}, 
        bash_command='psql -h postgres -U postgres -d data_warehouse -c "CREATE SCHEMA IF NOT EXISTS raw;"'
    )

    # 2. Run the Spark Script
    run_spark_ingest = BashOperator(
        task_id='spark_ingestion',
        # This path must match where you put the file in scripts/
        bash_command='python /opt/airflow/scripts/spark_ingestion.py'
    )

    create_schema >> run_spark_ingest