# copilot-agent-demo

A small Python ETL demo that reads customer and order CSV files, cleans the data,
builds a customer-level summary, and is intended to write the results to Snowflake.

## Pipeline

```text
data/customers.csv ──> ingest_customers ──> clean_customers ─┐
                                                            ├─> customer summary
data/orders.csv ─────> ingest_orders ─────> clean_orders ───┘
         │                     │                   │
         └─────────────────────┴───────────────────┴─> Snowflake tables
```

The entry point is `run_pipeline.py`. It runs these steps in order:

1. **Ingest** — `ingest.py` reads `customers.csv` and `orders.csv` from the
   repository's `data/` directory into pandas DataFrames.
2. **Transform** — `transform.py` normalizes and filters the input data, then
   joins customer records with order aggregates.
3. **Load** — the pipeline is intended to write three DataFrames to Snowflake:
   `STG_CUSTOMERS`, `STG_ORDERS`, and `CUSTOMER_SUMMARY`.

### Transformations

- Customers: trim and lowercase email addresses; trim and uppercase countries;
  parse `signup_date` as a datetime; keep the first row per `customer_id`; and
  drop rows missing `customer_id` or `email`.
- Orders: parse `order_date` as a datetime and `amount` as a number; drop rows
  missing `order_id`, `customer_id`, or `amount`; keep only positive amounts;
  and keep the first row per `order_id`.
- Customer summary: aggregate orders per customer to calculate order count,
  total spend, and first/last order dates. Customers without orders get zero
  for order count and spend. The summary contains `customer_id`, `email`,
  `country`, `total_orders`, `total_spent`, `first_order`, and `last_order`.

The CSV inputs are expected to have these columns:

| File | Columns used by the pipeline |
| --- | --- |
| `data/customers.csv` | `customer_id`, `email`, `country`, `signup_date` |
| `data/orders.csv` | `order_id`, `customer_id`, `order_date`, `amount` |

Additional input columns are retained in the respective cleaned customer or
order DataFrame, but are not included in the customer summary.

## Setup

Use Python with pandas and the Snowflake Connector for Python installed. There
is currently no dependency manifest in the repository.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pandas snowflake-connector-python
```

Put the input files in `data/` using the filenames and columns above. No sample
input data is included in this repository.

## Configuration

Snowflake connection settings are read from environment variables in
`config.py`:

| Variable | Required/default |
| --- | --- |
| `SNOWFLAKE_ACCOUNT` | Required for a Snowflake connection |
| `SNOWFLAKE_USER` | Required for a Snowflake connection |
| `SNOWFLAKE_PASSWORD` | Required for password authentication |
| `SNOWFLAKE_WAREHOUSE` | Defaults to `COMPUTE_WH` |
| `SNOWFLAKE_DATABASE` | Defaults to `DEMO_DB` |
| `SNOWFLAKE_SCHEMA` | Defaults to `ETL_DEMO` |
| `SNOWFLAKE_ROLE` | Optional; no default |

Do not put credentials in source files or commit them. For example, in
PowerShell, set credentials for the current terminal session with:

```powershell
$env:SNOWFLAKE_ACCOUNT = "<account>"
$env:SNOWFLAKE_USER = "<user>"
$env:SNOWFLAKE_PASSWORD = "<password>"
```

The default target names are `STG_CUSTOMERS`, `STG_ORDERS`, and
`CUSTOMER_SUMMARY`. The loader is configured to create tables automatically
and overwrite existing table contents on each load.

## Running

The intended command is:

```powershell
python run_pipeline.py
```

The entry point also defines `--dry-run`, intended to log row counts and sample
rows instead of loading data:

```powershell
python run_pipeline.py --dry-run
```

Logging is configured at INFO level. The transform functions can also be
imported and exercised independently with pandas DataFrames.

## Documentation

Project docs live under the repository's `docs/` directory:

- [docs/pipeline-overview.md](docs/pipeline-overview.md) — end-to-end ETL flow, environment variables, and known gaps
- [docs/models/customer-summary.md](docs/models/customer-summary.md) — model definition for `CUSTOMER_SUMMARY`

## Current repository limitations

The repository does not currently contain the files needed to run the entry
point end to end:

- `run_pipeline.py` imports `load_table` from `load.py`, but `load.py` is not
  present in the tracked files. A `load_table` implementation exists in
  `log.py`, but the entry point does not import it from there.
- The `data/` directory and the expected CSV input files are not included.
- There is no dependency manifest or automated test suite in the tracked files.

Consequently, the commands above describe the intended interface; the pipeline
will need the missing loader module and input CSVs before it can run. In
particular, `--dry-run` does not avoid the missing `load.py` import because
that import happens when the script starts.
