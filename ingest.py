"""INGEST: read raw files into DataFrames. No business logic here."""
import logging
 
import pandas as pd
 
from config import DATA_DIR
 
log = logging.getLogger(__name__)
 
 
def ingest_customers() -> pd.DataFrame:
    path = DATA_DIR / "customers.csv"
    df = pd.read_csv(path)
    log.info("Ingested %d rows from %s", len(df), path.name)
    return df
 
 
def ingest_orders() -> pd.DataFrame:
    path = DATA_DIR / "orders.csv"
    df = pd.read_csv(path)
    log.info("Ingested %d rows from %s", len(df), path.name)
    return df
 