# Airflow service

Structure of the project:
* 📁 src : folder of the analytocs to be copied on dags folder
* 📁 config dags plugins logs : empty folder to be created before starting airflow
* docker-compose.yml : docker compsoe file to start the airflow services

## 🎮 How To
    mkdir ./dags 
    mkdir ./logs 
    mkdir ./plugins 
    mkdir ./config

on linux
    echo -e "AIRFLOW_UID=$(id -u)" > .env

on windows 
    echo "AIRFLOW_UID=50000" > .env

🚩 on .env add apache-airflow-providers-influxdb

   docker compose up airflow-init
   docker compose up

to check
   docker ps --format '{{.Names}}'

to stop
   docker compose down --volumes --remove-orphans


## Http call to call airflow

    curl -X POST "http://localhost:8080/api/v1/dags/ruledag/dagRuns" -H  "accept: application/json" -H  "Content-Type: application/json" -d '{"conf":{}}' --user "airflow:airflow"