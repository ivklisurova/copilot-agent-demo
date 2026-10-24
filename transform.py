"""TRANSFORM: pure functions, DataFrame in -> DataFrame out (easy to unit test)."""
import pandas as pd


def clean_customers(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["email"] = out["email"].str.strip().str.lower()
    out["country"] = out["country"].str.strip().str.upper()
    out["signup_date"] = pd.to_datetime(out["signup_date"], errors="coerce")
    out = out.drop_duplicates(subset="customer_id")
    out = out.dropna(subset=["customer_id", "email"])
    return out


def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["order_date"] = pd.to_datetime(out["order_date"], errors="coerce")
    out["amount"] = pd.to_numeric(out["amount"], errors="coerce")
    out = out.dropna(subset=["order_id", "customer_id", "amount"])
    out = out[out["amount"] > 0]
    out = out.drop_duplicates(subset="order_id")
    return out


def build_customer_summary(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    agg = (
        orders.groupby("customer_id")
        .agg(
            total_orders=("order_id", "count"),
            total_spent=("amount", "sum"),
            first_order=("order_date", "min"),
            last_order=("order_date", "max"),
        )
        .reset_index()
    )
    summary = customers.merge(agg, on="customer_id", how="left")
    summary["total_orders"] = summary["total_orders"].fillna(0).astype(int)
    summary["total_spent"] = summary["total_spent"].fillna(0.0).round(2)
    return summary[
        ["customer_id", "email", "country", "total_orders", "total_spent", "first_order", "last_order"]
    ]