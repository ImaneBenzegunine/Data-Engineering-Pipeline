
Airflow — Admin Recovery & Quick Start

- **Symptom:** unable to log in to the Airflow UI even after running user creation commands.

Why this happens

- DB migrations can finish after the user creation command runs, or the command can silently fail. The result is an admin user that either doesn't exist or has no saved password.

Fix: create or reset admin user inside the Airflow container

```bash
# enter the running airflow container (compose name may differ)
docker exec -it airflow bash

# create or reset the admin user inside the container
airflow users create \
  --username admin \
  --password admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@test.com

exit
```

- Then open the UI at: http://localhost:8080

Quick start (if using Compose)

```powershell
cd airflow
docker compose up -d
```

If problems persist: check scheduler and webserver logs inside the container and ensure the metadata DB migrated successfully.
  --firstname Admin \













with spark : 
docker compose up --build -d;
airflow db init


docker exec -it airflow_webserver airflow users create --username admin --firstname Imane --lastname B --role Admin --email admin@example.com --password admin
