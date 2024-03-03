import datetime
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

def test_rule(**kwargs):
    """Print the Airflow context."""
    import logging
    logging.info("=>===========<=")
    logging.info(kwargs)
    logging.info("=>===========<=")
    source = kwargs['source']
    value = kwargs['value']
    threshold = kwargs['params']["threshold"]

    if float(value) >= float(threshold):
        logging.info("Anomaly {value} > {threshold} on {source}")

    return "My first DAG"

with DAG('ruledag', description='My First Rule DAG', 
    default_args = {'owner': 'iiot-book2'},
    start_date=days_ago(0),
    schedule_interval='@once') as dag:

    t1 = PythonOperator(task_id="test_rule",
                   provide_context=True,
                    python_callable=test_rule)