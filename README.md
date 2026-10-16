
# 🛒 E-Commerce Product Demand Analysis

## Overview
E-Commerce Product Demand Analysis is a Python-based project that analyzes product sales data and displays useful business insights through an interactive Streamlit dashboard.

It helps users understand product performance, sales trends, and estimated future demand.

## Objectives
- Calculate total units sold and total revenue.
- Identify best-selling products.
- Identify slow-moving products.
- Visualize daily product sales.
- Estimate product demand for the next week.
- Analyze changes in product demand.

## Technologies Used
- Python
- Streamlit
- Pandas
- CSV

## Project Structure

```text
EcommerceDemandAnalysis/
├── app.py
├── analysis.py
├── forecast.py
├── orders.csv
├── requirements.txt
└── README.md
```

## Installation

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Run the application

```powershell
python -m streamlit run app.py --server.port 8503
```

### 4. Open the dashboard

Visit:

http://localhost:8503

## Dataset Format

The `orders.csv` file must contain these columns:

| Column | Description |
|---|---|
| order_date | Date of the order |
| product_name | Name of the product |
| quantity | Number of units sold |
| unit_price | Price per unit |

Example:

```csv
order_date,product_name,quantity,unit_price
2026-10-01,Laptop,2,50000
2026-10-02,Mouse,10,500
2026-10-03,Keyboard,5,1200
```

## Main Features

### Sales Performance
Displays total units sold, total revenue, and the number of products.

### Best-Selling Products
Ranks products according to their total quantity sold.

### Slow-Moving Products
Lists products from lowest to highest quantity sold.

### Product Demand Analysis
Displays daily sales trends for a selected product.

### Demand Forecast
Estimates next-week demand using recent sales history.

### Demand Change Alert
Compares recent weekly sales with the previous week when sufficient historical data is available.

## Purpose and Applications

This project demonstrates how sales data analysis can support inventory planning, stock management, and business decision-making.

## Limitations
- Forecasts are estimates and may not reflect actual future demand.
- Results depend on the quality and quantity of the input data.
- The sample dataset is for demonstration and does not represent actual business sales.

## Future Enhancements
- Use larger real-world datasets.
- Add interactive date filters.
- Implement advanced forecasting algorithms.
- Add downloadable sales reports.
- Connect the dashboard to a database.

## Author
Student Project — E-Commerce Product Demand Analysis
