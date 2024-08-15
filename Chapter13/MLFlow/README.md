


## Connect to MLFlow to serve model

Connect to mlflow_server
      docker compose --env-file config.env exec mlflow_server /bin/bash

now we can serve the model
     mlflow models serve -m models:/wind_turbine/1 -p 5001                        