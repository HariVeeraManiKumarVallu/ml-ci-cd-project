from fastapi import FastAPI
import joblib
from pydantic import BaseModel, conlist
import os
from datetime import datetime
from typing import List

app = FastAPI()
model = joblib.load('models/model.pkl')

MODEL_VERSION = "1.0"
MODEL_TRAINED_ON = os.path.getmtime("models/model.pkl")  # Unix timestamp

class IrisInput(BaseModel):
    data: conlist(float, min_length=4, max_length=4)  # Exactly 4 floats

class PredictionOutput(BaseModel):
    prediction: int

@app.post("/predict", response_model=PredictionOutput)
def predict(input: IrisInput):
    prediction = model.predict([input.data])
    return {"prediction": int(prediction[0])}

@app.get("/health", summary="Health check", description="Check if the API is running")
def health():
    return {"status": "ok"}

@app.get("/model-info", summary="Model info", description="Get model version and training date")
def model_info():
    trained_on = datetime.fromtimestamp(MODEL_TRAINED_ON).isoformat()
    return {"version": MODEL_VERSION, "trained_on": trained_on}