from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator

# If your 'extract_to_s3.py' file has a function named 'main' or 'extract', 
# you can import it here. Otherwise, we use a placeholder function below.
# from extract_to_s3 import extract_data_function

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 10, 22),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def mock_extract_and_push_to_s3():
    """
    Placeholder function. Replace this print statement with your actual 
    code from extract_to_s3.py to fetch from CoinGecko and upload to AWS S3.
    """
    print("Extracting crypto prices from CoinGecko API and saving to S3...")

def mock_load_s3_to_postgres():
    """
    Placeholder function. Replace this with your logic to download data 
    from S3 and insert it into your PostgreSQL table.
    """
    print("Loading data from S3 bucket into PostgreSQL fact_crypto_prices table...")

with DAG(
    dag_id='fetch_crypto_and_push_to_s3',
    default_args=default_args,
    description='A portfolio crypto pipeline extracting data to S3 and Postgres',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    # TASK 1: Automatically creates the target database table if it does not exist
    create_table = PostgresOperator(
        task_id="create_crypto_table",
        postgres_conn_id="postgres_default",  # Ensure this matches your Airflow Connection UI
        sql="""
        CREATE TABLE IF NOT EXISTS fact_crypto_prices (
            id SERIAL PRIMARY KEY,
            coin_id VARCHAR(50) NOT NULL,
            coin_name VARCHAR(100) NOT NULL,
            price_eur NUMERIC(16, 4) NOT NULL,
            extracted_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        );
        """
    )

    # TASK 2: Runs your script to grab CoinGecko data and store it in AWS S3
    extract_and_push_s3 = PythonOperator(
        task_id="extract_crypto_to_s3",
        python_callable=mock_extract_and_push_to_s3,  # Link your s3 logic here
    )

    # TASK 3: Copies or inserts the data from S3 into your Postgres database
    load_to_postgres = PythonOperator(
        task_id="load_s3_to_postgres",
        python_callable=mock_load_s3_to_postgres,  # Link your database insert logic here
    )

    # Definitive workflow step execution order
    create_table >> extract_and_push_s3 >> load_to_postgres
