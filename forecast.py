
import pandas as pd


def forecast_next_week(df, product_name):
    """Estimate next week's demand using recent daily sales."""

    product_df = df[
        df["product_name"] == product_name
    ].copy()

    if product_df.empty:
        return None

    product_df["order_date"] = pd.to_datetime(
        product_df["order_date"], errors="coerce"
    )

    product_df = product_df.dropna(
        subset=["order_date", "quantity"]
    )

    if product_df.empty:
        return None

    daily_sales = (
        product_df.set_index("order_date")["quantity"]
        .resample("D")
        .sum()
        .sort_index()
    )

    if len(daily_sales) < 7:
        return None

    # Estimate demand from the most recent 7 days.
    last_week = daily_sales.tail(7)
    estimated_next_week = last_week.mean() * 7

    return max(0, float(estimated_next_week))


def demand_change(df, product_name):
    """Compare the latest 7 days with the preceding 7 days."""

    product_df = df[
        df["product_name"] == product_name
    ].copy()

    if product_df.empty:
        return None

    product_df["order_date"] = pd.to_datetime(
        product_df["order_date"], errors="coerce"
    )

    product_df["quantity"] = pd.to_numeric(
        product_df["quantity"], errors="coerce"
    )

    product_df = product_df.dropna(
        subset=["order_date", "quantity"]
    )

    if product_df.empty:
        return None

    daily_sales = (
        product_df.set_index("order_date")["quantity"]
        .resample("D")
        .sum()
        .sort_index()
    )

    if len(daily_sales) < 14:
        return None

    recent_week = daily_sales.tail(7).sum()
    previous_week = daily_sales.iloc[-14:-7].sum()

    if previous_week == 0:
        if recent_week == 0:
            return 0.0
        return None

    change = (
        (recent_week - previous_week)
        / previous_week
    ) * 100

    return float(change)
