from fastapi import FastAPI
import mlflow
import pandas as pd
import numpy as np

app = FastAPI()
@app.post("/predict")
async def predict(X_test:float) -> list:
    logged_model = f'models:/wind_turbine/1'
    
    loaded_model = mlflow.pyfunc.load_model(logged_model)
    return list(loaded_model.predict(np.array([X_test]).reshape(-1, 1)))
