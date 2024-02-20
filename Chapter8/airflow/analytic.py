from datetime import datetime from airflow import DAG 
from airflow.operators.dummy_operator import DummyOperator 
from airflow.operators.python_operator import PythonOperator
from airflow.operators import InlfuxDBOperator 
import datetime import logging 

def my_mean(ds, **kwargs): 
    logging.info("kwargs: %s" % kwargs) 
    logging.info("ds: %s" % ds) 
    ti = kwargs['ti'] 
    data = ti.xcom_pull(key=None, task_ids=['get_data']) return _mean(data) 

def _mean(data): ret={} 

    for d in data: 

        results = d['results'] for r in results: 

        m = [float(sum(l))/len(l) for l in zip(*r['values'])] ret[r['name']] = m[1] 

        print(ret) 
        return ret 

    dag = DAG('mymean', description='Simple Mean of the temperature from last year', 
    default_args = {'owner': 'iiot-book'}, schedule_interval='* * * * 0', start_date=datetime.datetime(2018, 6, 21), catchup=False) 

    influxdb_operator = InfluxDBOperator( 
        task_id='get_data', query={ "metrics": [ { "tags": {}, "name": "device0.my.measure.temperature", "aggregators": 
        [{"name": "scale", "factor": "1.0"}]}], "plugins": [], "cache_time": 0, "start_relative": { "value": "1", "unit": "years"}}, dag=dag) 

    myanalytic_task= PythonOperator(task_id='myanalytic', provide_context=True, python_callable=print_context, dag=dag) 