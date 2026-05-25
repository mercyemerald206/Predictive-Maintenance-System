from fastapi import FastAPI
import random

app = FastAPI(title="Predictive Maintenance Service")

@app.get("/predict")
def predict():
    vibration = random.uniform(0, 1)
    temperature = random.uniform(20, 120)

    risk = (vibration * 0.6) + (temperature / 120 * 0.4)

    return {
        "vibration": round(vibration, 3),
        "temperature": round(temperature, 2),
        "failure_risk": round(risk, 3),
        "status": "HIGH RISK" if risk > 0.7 else "SAFE"
    }
