#!/usr/bin/env bash
# Wait for the DB to be ready
echo "Waiting for Airflow DB to be ready..."
sleep 10

# Try to create admin user (will not fail if it exists)
airflow users create \
    --username admin \
    --password admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@test.com || true
