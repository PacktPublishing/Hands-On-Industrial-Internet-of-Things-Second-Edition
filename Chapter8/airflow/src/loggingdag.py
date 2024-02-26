import datetime
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

def print_context(**kwargs):
    """Print the Airflow context."""
    import logging
    logging.info("=>===========<=")
    logging.info(kwargs)
    return "My first DAG"

with DAG('loggingdag', description='Simple Logging DAG', 
    default_args = {'owner': 'iiot-book2'},
    start_date=days_ago(0),
    schedule_interval='*/1 * * * *') as dag:

    t1 = PythonOperator(task_id="print_the_context",
                   provide_context=True,
                    python_callable=print_context)
    
    t2 = PythonOperator(task_id="print_without_context",
                python_callable=print_context)
    
    t1 >> t2