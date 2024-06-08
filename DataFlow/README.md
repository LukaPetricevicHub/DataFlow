# DataFlow

## Description

DataFlow is an ETL (Extract, Transform, Load) pipeline project that transfers sales data from a MySQL database to an Apache Hive data warehouse. The pipeline is orchestrated using Apache Airflow.

## Setup Instructions

### Prerequisites

- MySQL Server
- Apache Hive
- Apache Airflow
- Python 3.x

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/LukaPetricevicHub/DataFlow.git
    cd DataFlow
    ```

2. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up MySQL database and table:
    ```bash
    mysql -u root -p < sql_scripts/create_mysql_tables.sql
    ```

4. Set up Hive database and table:
    ```bash
    hive -f sql_scripts/create_hive_tables.sql
    ```

5. Configure Airflow:
    - Follow the official [Apache Airflow Installation](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html) guide.
    - Place the `sales_etl.py` DAG file in the Airflow DAGs folder.

## Usage Instructions

1. Start Airflow services:
    ```bash
    airflow scheduler
    airflow webserver
    ```

2. Access the Airflow web UI and trigger the `sales_etl` DAG to run the ETL pipeline.