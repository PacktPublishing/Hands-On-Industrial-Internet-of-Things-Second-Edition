

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

to check
   docker ps --format '{{.Names}}'

to stop
   docker compose down --volumes --remove-orphans



## external run

    curl -X POST "http://localhost:8080/api/v1/dags/ruledag/dagRuns" -H  "accept: application/json" -H  "Content-Type: application/json" -d '{"conf":{}}' --user "airflow:airflow"