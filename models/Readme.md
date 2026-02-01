Models & Layers (dbt)

This project follows a common layered approach:

- **Source:** raw input (Airbyte, local CSVs)
- **Bronze:** raw tables with load timestamps (traceability)
- **Silver:** cleaned and typed staging tables
- **Gold:** analytics-ready models (facts/dimensions)

Why this matters

- Lineage: you can trace any dashboard row back to the gold → silver → bronze → source.

Running dbt (example)

```bash
# from the dbt project root
dbt deps
dbt seed   # if seeds exist
dbt run
dbt test
```

Layer	Responsibility	Input	Output
Source-	External Reality	-Airbyte/Kaggle-	Raw Tables
Bronze-	Traceability	-Source           -	Tables + Load Timestamps
Silver-	Consistency	-Bronze               - 	Cleaned/Typed Tables
Gold -	Analytics	-Silver	               -Business Metrics/Joins


Engineering Mindset Check:
By doing this, you have created a Lineage.
If someone asks: "Where did this row in the dashboard come from?" you can trace it:
Gold (Fact table)
Silver (Staging - where it was cleaned)
Bronze (Buffer - where the raw CSV was first seen)
Source (Airbyte - the external tool)