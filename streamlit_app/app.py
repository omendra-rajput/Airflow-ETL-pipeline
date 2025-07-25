import streamlit as st
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from datetime import datetime, timedelta

st.set_page_config(page_title="Stock Dashboard", layout="wide")
st.title("Real-Time Stock Tracker")

# User input
symbol = st.text_input("Enter Stock Symbol:", value="TSLA")

# KPI placeholders
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric(label="Last Close Price", value="$650", delta="+2.3%")
kpi2.metric(label="Day Low", value="$625")
kpi3.metric(label="Day High", value="$665")

# Sample placeholder chart
st.subheader("Price Trend (Last 10 Days)")
dates = pd.date_range(end=datetime.today(), periods=10)
fake_prices = np.linspace(620, 670, 10) + np.random.normal(0, 5, 10)
placeholder_df = pd.DataFrame({"Date": dates, "Close": fake_prices})
st.line_chart(placeholder_df.set_index("Date")["Close"])

# Load real data
if st.button("Load Real Stock Data"):
    try:
        engine = create_engine("postgresql+psycopg2://airflow:airflow@localhost:5433/stockdb")
        query = f"SELECT * FROM stock_data WHERE symbol = '{symbol.upper()}'"
        df = pd.read_sql(query, engine)

        if not df.empty:
            st.success(f"Loaded {len(df)} records from the database.")

            df["Date"] = pd.to_datetime(df["Date"])
            latest = df.sort_values("Date").iloc[-1]
            previous = df.sort_values("Date").iloc[-2]

            kpi1.metric(
                label="Last Close Price",
                value=f"${latest['Close']:.2f}",
                delta=f"{((latest['Close'] - previous['Close']) / previous['Close']) * 100:.2f}%"
            )
            kpi2.metric(label="Day Low", value=f"${latest['Low']:.2f}")
            kpi3.metric(label="Day High", value=f"${latest['High']:.2f}")

            st.subheader(f"Price Trend for {symbol.upper()}")
            st.line_chart(df.set_index("Date")["Close"])
            st.dataframe(df.tail(10))
        else:
            st.warning("No data found for the entered symbol.")
    except Exception as e:
        st.error(f"Failed to load data: {e}")
