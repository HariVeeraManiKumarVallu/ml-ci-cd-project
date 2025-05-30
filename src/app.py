from fastapi import FastAPI
import joblib
from pydantic import BaseModel

app = FastAPI()
model = joblib.load('models/model.pkl')

class IrisInput(BaseModel):
    data: list

@app.post("/predict")
def predict(input: IrisInput):
    prediction = model.predict([input.data])
    return {"prediction": int(prediction[0])}