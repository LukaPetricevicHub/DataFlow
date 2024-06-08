import pandas as pd
import mysql.connector
from pyhive import hive
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

# MySQL connection details
mysql_conn_details = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'sales_db'
}

# Hive connection details
hive_conn_details = {
    'host': 'localhost',
    'port': 10000,
    'username': 'hive',
    'database': 'sales_dw'
}

def extract_data():
    conn = mysql.connector.connect(**mysql_conn_details)
    query = "SELECT region, SUM(amount) as total_amount FROM sales GROUP BY region"
    df = pd.read_sql(query, conn)
    conn.close()
    df.to_csv('/tmp/aggregated_sales.csv', index=False)

def load_data():
    conn = hive.Connection(**hive_conn_details)
    cursor = conn.cursor()
    cursor.execute("LOAD DATA LOCAL INPATH '/tmp/aggregated_sales.csv' INTO TABLE aggregated_sales")
    cursor.close()
    conn.close()

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

dag = DAG(
    'sales_etl',
    default_args=default_args,
    description='A simple sales ETL pipeline',
    schedule_interval='@daily',
)

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

extract_task >> load_task