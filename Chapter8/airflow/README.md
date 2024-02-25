

    mkdir ./dags 
    mkdir ./logs 
    mkdir ./plugins 
    mkdir ./config

on linux
    echo -e "AIRFLOW_UID=$(id -u)" > .env

on windows 
    echo "AIRFLOW_UID=50000" > .env


on .env add apache-airflow-providers-influxdb

   docker compose up airflow-init
   docker compose up


to stop
   docker compose down --volumes --remove-orphans