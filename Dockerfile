FROM apache/airflow:2.8.1-python3.10

# Switch to airflow user first
USER airflow

# Install your required Python packages
RUN pip install --no-cache-dir \
    yfinance \
    pandas \
    sqlalchemy \
    psycopg2-binary
