
import streamlit as st
import pandas as pd
from pathlib import Path

from analysis import (
    load_data,
    best_selling_products,
    slow_moving_products,
)
from forecast import forecast_next_week, demand_change

st.set_page_config(
    page_title="E-Commerce Product Demand Analysis",
    page_icon="📊",
    layout="wide",
)

st.title("🛒 E-Commerce Product Demand Analysis")
st.write("Analyze product sales, demand trends, and future demand.")

# Always load the CSV from the project folder
DATA_FILE = Path(__file__).resolve().parent / "orders.csv"

try:
    df = load_data(str(DATA_FILE))
except Exception as e:
    st.error(f"Could not load orders.csv: {e}")
    st.stop()

if df.empty:
    st.warning("No valid order data found. Please check orders.csv.")
    st.stop()

# Key performance indicators
total_units = int(df["quantity"].sum())
total_revenue = float(df["revenue"].sum())
total_products = df["product_name"].nunique()

c1, c2, c3 = st.columns(3)
c1.metric("Total Units Sold", f"{total_units:,}")
c2.metric("Total Revenue", f"₹{total_revenue:,.2f}")
c3.metric("Products", total_products)

st.divider()

# Best-selling products
st.subheader("🏆 Best-Selling Products")
best = best_selling_products(df)
st.bar_chart(best.set_index("product_name")["quantity"])
st.dataframe(best, use_container_width=True)

# Slow-moving products
st.subheader("🐢 Slow-Moving Products")
st.dataframe(
    slow_moving_products(df),
    use_container_width=True,
)

st.divider()

# Product demand analysis
st.subheader("📈 Product Demand Analysis")

products = sorted(df["product_name"].dropna().unique().tolist())

if not products:
    st.warning("No products found in the CSV.")
    st.stop()

product = st.selectbox("Choose a product", products)

product_df = df[df["product_name"] == product].copy()

daily_sales = (
    product_df.set_index("order_date")["quantity"]
    .resample("D")
    .sum()
)

st.line_chart(daily_sales)

# Next-week demand forecast
st.subheader("🔮 Next-Week Demand Forecast")

try:
    forecast_value = forecast_next_week(df, product)

    if forecast_value is None:
        st.info("Not enough historical data to forecast reliably.")
    else:
        st.metric(
            "Estimated Units Next Week",
            f"{forecast_value:.0f}",
        )
except Exception as e:
    st.warning(f"Forecast unavailable: {e}")

# Demand change alert
st.subheader("🚨 Demand Change Alert")

try:
    change = demand_change(df, product)

    if change is None:
        st.info("Not enough data to calculate demand change.")
    else:
        st.metric("Demand Change", f"{change:+.1f}%")

        if change >= 20:
            st.success("Demand has increased significantly!")
        elif change <= -20:
            st.warning("Demand has decreased significantly.")
        else:
            st.info("No significant demand change detected.")
except Exception as e:
    st.warning(f"Demand-change analysis unavailable: {e}")

# Raw order data
with st.expander("View Order Data"):
    st.dataframe(df, use_container_width=True)
