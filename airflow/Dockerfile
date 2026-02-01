#FROM apache/airflow:latest
FROM apache/airflow:2.8.1

USER root

# Ensure scripts can be executed
RUN mkdir -p /opt/airflow/scripts
COPY create_admin_user.sh /opt/airflow/scripts/
RUN chmod +x /opt/airflow/scripts/create_admin_user.sh

USER airflow
