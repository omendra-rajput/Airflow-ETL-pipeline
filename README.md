# Stock ETL Pipeline with Apache Airflow

This project demonstrates a containerized ETL pipeline for stock market data using Apache Airflow and PostgreSQL. The pipeline extracts stock data via an API (e.g., Yahoo Finance), transforms it into a structured format, loads it into a PostgreSQL database, and visualizes it through a Streamlit dashboard.

## Project Structure

stock-etl/
│
├── dags/ # Airflow DAG definitions
│ └── stock_etl_dag.py
│
├── data/ # Extracted raw and transformed stock data
│
├── logs/ # Airflow logs
│
├── plugins/ # Custom plugins (if any)
│
├── Dockerfile # Dockerfile for Airflow components
├── docker-compose.yaml # Orchestrates all services
├── requirements.txt # Python dependencies
└── README.md # Project documentation


## Features

- Modular ETL pipeline using Apache Airflow
- PostgreSQL for structured data storage
- Redis (optional) for Airflow queues
- Streamlit app for visualizing stock metrics
- Dockerized deployment with minimal setup

## Services

| Service           | Description                              | Port     |
|-------------------|------------------------------------------|----------|
| Airflow Webserver | Workflow orchestration UI                | 8090     |
| PostgreSQL        | Stock data storage                       | 5433     |
| Redis             | Task queue for Airflow (if used)         | 6379     |

## Prerequisites

- Docker Desktop (with WSL2 backend if on Windows)
- Docker Compose
- Python 3.8+ (for local testing and DAG logic development)

## Getting Started

### 1. Clone the Repository

git clone https://github.com/yourusername/stock-etl.git
cd stock-etl
### 2. Build and Start Services
bash
Copy
Edit
docker compose up --build
Airflow Web UI will be accessible at:
http://localhost:8090

### 3. Initialize Airflow Database
bash
Copy
Edit
docker exec -it airflow-webserver airflow db init
### 4. Create Admin User
bash
Copy
Edit
docker exec -it airflow-webserver airflow users create \
  --username admin \
  --firstname Omendra \
  --lastname Rajput \
  --role Admin \
  --email omendra@example.com \
  --password airflow
### 5. Verify DAG
Check the Airflow UI at localhost:8090 and ensure your DAG stock_etl_dag is listed. Enable and trigger it.

Technologies Used
Apache Airflow 2.9.1

PostgreSQL 13

Redis 7 (optional)

Docker + Docker Compose

Python 3.10

Pandas, Requests (for data handling)

Streamlit (for dashboard visualization)

Use Case
Monitor and analyze stock performance using live and historical market data.

Automate data collection and processing using scheduled DAGs.

Use PostgreSQL for structured querying and analytics.










