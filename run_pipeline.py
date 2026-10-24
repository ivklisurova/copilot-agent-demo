"""Orchestrates ingest -> transform -> load. Run with:  python run_pipeline.py [--dry-run]"""
import argparse
import logging

from config import TABLE_CUSTOMERS, TABLE_CUSTOMER_SUMMARY, TABLE_ORDERS
from ingest import ingest_customers, ingest_orders
from load import load_table
from transform import build_customer_summary, clean_customers, clean_orders

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("pipeline")


def main(dry_run: bool = False) -> None:
    # 1. Ingest
    raw_customers = ingest_customers()
    raw_orders = ingest_orders()

    # 2. Transform
    customers = clean_customers(raw_customers)
    orders = clean_orders(raw_orders)
    summary = build_customer_summary(customers, orders)

    # 3. Load into different tables
    targets = [
        (customers, TABLE_CUSTOMERS),
        (orders, TABLE_ORDERS),
        (summary, TABLE_CUSTOMER_SUMMARY),
    ]
    for df, table in targets:
        if dry_run:
            log.info("[dry-run] would load %d rows into %s\n%s", len(df), table, df.head(3))
        else:
            load_table(df, table)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Skip Snowflake load, just print")
    main(parser.parse_args().dry_run)