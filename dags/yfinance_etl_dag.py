from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

def fetch_and_store_stock(symbol: str = 'AAPL'):
    df = yf.download(symbol, period='5d', interval='1d')
    df.reset_index(inplace=True)
    df['symbol'] = symbol

    # Save to PostgreSQL — using 'airflow' DB (default)
    engine = create_engine("postgresql+psycopg2://airflow:airflow@postgres:5432/airflow")
    df.to_sql("stock_data", engine, if_exists='append', index=False)
    print(f" {symbol} data saved to PostgreSQL.")

default_args = {
    'owner': 'omendra',
    'start_date': datetime(2024, 1, 1),
}

with DAG('yfinance_etl_dag',
         schedule_interval=None,
         catchup=False,
         default_args=default_args,
         tags=['etl', 'yfinance'],
         description="ETL pipeline for stock data",
         ) as dag:

    fetch_stock_task = PythonOperator(
        task_id='fetch_stock_data',
        python_callable=fetch_and_store_stock,
        op_kwargs={'symbol': 'TSLA'}
    )
