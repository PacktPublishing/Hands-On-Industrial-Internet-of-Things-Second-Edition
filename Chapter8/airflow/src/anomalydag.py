import datetime
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.providers.influxdb.hooks.influxdb import InfluxDBHook

SQL = '''
from(bucket: "iiot-book-2")
  |> range(start: {start}, stop: {stop})
  |> filter(fn: (r) => r["topic"] == "{sensor_name}")
  |> aggregateWindow(every: 1h, fn: mean, createEmpty: true)
  |> yield(name: "mean")'''

 
def ad_by_quantile():

    import numpy as np
    import logging
    class SimplePercentileAD:

        def fit(self, X, y=None):
            percentile_range = (5, 95)
            self.percentiles = np.percentile(X, percentile_range)
            return self

        def predict(self, X):
            anomalies = np.where((X < self.percentiles[0]) | (X > self.percentiles[1]))
            return anomalies

    model = SimplePercentileAD()

    SENSOR_NAME='sensors/edge1/cpu/0'
    #train
    df = InfluxDBHook(conn_id="influxdb").query_to_df(SQL.format(start="-1h", stop="-5m", sensor_name=SENSOR_NAME))

    model.fit(df['_value'].values)

    #test
    df = InfluxDBHook(conn_id="influxdb").query_to_df(SQL.format(start="-5m", stop="0m", sensor_name=SENSOR_NAME))
    anomalies = model.predict(df['_value'].values)

    ret = f"ANOMALIES: found {np.sum(anomalies)} on {SENSOR_NAME}"

    logging.info("=============")
    logging.info(ret)
    logging.info("=============")

    return ret

with DAG('anomalydag', description='Simple Anomaly Detection DAG', 
    default_args = {'owner': 'iiot-book2'},
    start_date=days_ago(0),
    schedule_interval='*/1 * * * *') as dag:

    t1 = PythonOperator(task_id="ad_CPU_by_quantile",
                    provide_context=True,
                    python_callable=ad_by_quantile)
    
    t1