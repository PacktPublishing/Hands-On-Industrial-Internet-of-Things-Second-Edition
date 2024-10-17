# Using MLflow to deploy analytics

:whale2: docker-compose.yml: docker compose for jupyter notebook, minio and MLflow
:whale2: Dmlflow/ockerfile: Dockerfile for MLflow image
:file_folder: work: code 

## Start Server

Start servers:
      docker-compose --env-file config.env up -d --build 

## Connect to MLFlow to serve model

Connect to mlflow_server
     docker compose --env-file config.env exec mlflow_server /bin/bash

now we can serve the model
     mlflow models serve -m models:/wind_turbine/latest -h 0.0.0.0 -p 5001                        