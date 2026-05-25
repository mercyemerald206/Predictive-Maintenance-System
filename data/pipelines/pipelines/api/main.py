from fastapi import FastAPI
import numpy as np
from tensorflow.keras.models import load_model

app = FastAPI()
model = load_model("model/lstm_model.h5")

@app.post("/predict")
def predict(data: dict):
    arr = np.array([[data["temp"], data["volt"]]])
    arr = arr.reshape((1,1,2))

    pred = model.predict(arr)[0][0]
    return {"failure_risk": float(pred)}
