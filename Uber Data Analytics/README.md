# Uber Data Analytics

An ETL pipeline that turns a raw Uber trip CSV into a dimensional model in BigQuery, then
queries it for ride patterns. Built with Mage.ai on a GCP Compute Engine VM.

Built by following a public tutorial, so treat it as a worked exercise in dimensional
modelling and Mage.ai rather than original design.

## Pipeline

Mage.ai runs three blocks in sequence. Each file in `maze/` is one block.

1. `extract.py` loads `data/uber_data.csv` into a DataFrame and parses the pickup and
   dropoff timestamps.
2. `transform.py` splits the flat table into a star schema: dimension tables for datetime,
   passenger count, trip distance, rate code, pickup and dropoff location, and payment
   type, plus a central fact table holding the foreign keys and the fare columns.
3. `load.py` writes every table to BigQuery under
   `uber-project-falcon.uber_data_engineering_yt`, replacing the table if it exists.

`data_model.jpeg` is the schema diagram. `architecture.jpg` is the GCP layout.

## Querying

`query_sql.sql` builds an analytics view over the joined star schema and answers questions
about fare totals, trip distance, and pickup and dropoff patterns.

## Running it

`commands.txt` has the VM setup as it was run. The short version:

```
python3 -m venv venv && source venv/bin/activate
pip install mage-ai pandas google-cloud-bigquery
mage start <project-name>
```

Then open Mage on port 6789, point the pipeline at `data/uber_data.csv`, and put a GCP
service account key in `io_config.yaml`.

`io_config.yaml` holds credentials and is gitignored. It is not in this repo, and it should
never be committed.

## Stack

Python, Mage.ai, pandas, Google BigQuery, SQL, GCP Compute Engine.
