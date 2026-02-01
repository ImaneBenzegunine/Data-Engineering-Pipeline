kaggle datasets download -d olistbr/brazilian-ecommerce -p C:\imane\TYTHON\Project_data\kaggle\data   --unzip
___________________________________
Kaggle dataset & data placement

Download example dataset (replace with the dataset you need):

```powershell
kaggle datasets download -d olistbr/brazilian-ecommerce -p C:\imane\TYTHON\Project_data\kaggle\data --unzip
```

Organize CSVs for Airbyte/dbt

```powershell
mkdir -p C:\imane\TYTHON\Project_data\kaggle\data\row
move C:\imane\TYTHON\Project_data\kaggle\data\*.csv C:\imane\TYTHON\Project_data\kaggle\data\row
```

Notes

- Place your `kaggle.json` (API credentials) in this folder if using the CLI.
- The folder `kaggle/data/row` is mounted into Airbyte server for local-file sources; keep raw CSVs there.




