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