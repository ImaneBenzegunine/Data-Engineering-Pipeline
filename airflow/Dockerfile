FROM apache/airflow:2.7.1-python3.9

USER root
# Install Java 17 (Required for PySpark 4.0+)
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get clean

USER airflow
# Install PySpark
RUN pip install pyspark