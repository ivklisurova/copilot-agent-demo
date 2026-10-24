"""Central config. Secrets come from environment variables, never hard-code them."""
import os
from pathlib import Path
 
DATA_DIR = Path(__file__).parent / "data"
 
SNOWFLAKE = {
    "account": os.environ.get("SNOWFLAKE_ACCOUNT"),
    "user": os.environ.get("SNOWFLAKE_USER"),
    "password": os.environ.get("SNOWFLAKE_PASSWORD"),
    "warehouse": os.environ.get("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH"),
    "database": os.environ.get("SNOWFLAKE_DATABASE", "DEMO_DB"),
    "schema": os.environ.get("SNOWFLAKE_SCHEMA", "ETL_DEMO"),
    "role": os.environ.get("SNOWFLAKE_ROLE"),
}
 
# Target tables
TABLE_CUSTOMERS = "STG_CUSTOMERS"
TABLE_ORDERS = "STG_ORDERS"
TABLE_CUSTOMER_SUMMARY = "CUSTOMER_SUMMARY"
 