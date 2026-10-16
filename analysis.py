
import pandas as pd

REQUIRED_COLUMNS = [
    "order_date",
    "product_name",
    "quantity",
    "unit_price",
]


def load_data(file_path="orders.csv"):
    """Load and clean the order data."""
    df = pd.read_csv(file_path)

    missing = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    df["order_date"] = pd.to_datetime(
        df["order_date"], errors="coerce"
    )
    df["quantity"] = pd.to_numeric(
        df["quantity"], errors="coerce"
    )
    df["unit_price"] = pd.to_numeric(
        df["unit_price"], errors="coerce"
    )

    df = df.dropna(subset=REQUIRED_COLUMNS).copy()
    df = df[
        (df["quantity"] >= 0)
        & (df["unit_price"] >= 0)
    ]

    df["revenue"] = df["quantity"] * df["unit_price"]

    return df


def best_selling_products(df):
    """Rank products by highest quantity sold."""
    return (
        df.groupby("product_name", as_index=False)
        .agg(
            quantity=("quantity", "sum"),
            revenue=("revenue", "sum"),
        )
        .sort_values("quantity", ascending=False)
    )


def slow_moving_products(df):
    """Rank products by lowest quantity sold."""
    return (
        df.groupby("product_name", as_index=False)
        .agg(
            quantity=("quantity", "sum"),
            revenue=("revenue", "sum"),
        )
        .sort_values("quantity", ascending=True)
    )


def monthly_demand(df, product_name):
    """Calculate monthly demand for one product."""
    product_df = df[
        df["product_name"] == product_name
    ].copy()

    if product_df.empty:
        return pd.Series(dtype="float64")

    return (
        product_df.set_index("order_date")["quantity"]
        .resample("MS")
        .sum()
    )
