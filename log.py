"""LOAD: write DataFrames to Snowflake tables."""
import logging

import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

from config import SNOWFLAKE

log = logging.getLogger(__name__)


def get_connection():
    return snowflake.connector.connect(**{k: v for k, v in SNOWFLAKE.items() if v})


def load_table(df: pd.DataFrame, table: str, overwrite: bool = True) -> int:
    """Load a DataFrame into `table`. Creates the table if it doesn't exist."""
    df = df.copy()
    df.columns = [c.upper() for c in df.columns]  # Snowflake-friendly column names

    conn = get_connection()
    try:
        success, _, nrows, _ = write_pandas(
            conn,
            df,
            table_name=table,
            auto_create_table=True,
            overwrite=overwrite,
            use_logical_type=True,  # keeps timestamps as proper TIMESTAMP types
        )
        log.info("Loaded %d rows into %s (success=%s)", nrows, table, success)
        return nrows
    finally:
        conn.close()