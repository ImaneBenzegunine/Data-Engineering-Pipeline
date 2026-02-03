Set Up Python Environment
3. Create and Activate Virtual Environment (Windows)
Project Data — Quick Start

- **Overview:** This workspace contains data ingestion (Airbyte), orchestration (Airflow), datasets (Kaggle), dbt models, and helper scripts.
- **Prerequisites:** Docker, Docker Compose, Python 3.8+ (for local scripts), and optionally `abctl` for Airbyte local installs.

Setup (Windows)

- Create & activate a virtual environment:

```powershell
python -m venv .venv
venv\Scripts\activate
```

- Install Python dependencies:

```powershell
pip install -r requirements.txt
```

Project layout

- `Airbyte/` — local Airbyte compose and helpers
- `airflow/` — Airflow Dockerfile and DAGs
- `kaggle/` — kaggle credentials and raw dataset folder
- `dbt/`, `models/` — dbt project and SQL models

If you want, I can add a consolidated `CONTRIBUTING.md` or a launch script next.