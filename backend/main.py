from fastapi import FastAPI
from pydantic import BaseModel
import sys
import os

# Add ml folder to Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from ml.agromind_engine import agromind_recommend
from backend.weather_api import get_weather
app = FastAPI(title="AgroMind API")


# -----------------------------
# Request schema
# -----------------------------
class SoilInput(BaseModel):
    N: float
    P: float
    K: float
    ph: float
    city: str


# -----------------------------
# Root test route
# -----------------------------
@app.get("/")
def home():
    return {"message": "AgroMind API is running"}


# -----------------------------
# Prediction route
# -----------------------------
@app.post("/predict")
def predict(data: SoilInput):

    temperature, humidity, rainfall = get_weather(data.city)

    result = agromind_recommend(
        data.N,
        data.P,
        data.K,
        temperature,
        humidity,
        data.ph,
        rainfall
    )

    result["weather"] = {
        "temperature": temperature,
        "humidity": humidity,
        "rainfall": rainfall
    }

    return result