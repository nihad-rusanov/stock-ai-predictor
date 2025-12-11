from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import tensorflow as tf
import joblib

from backend.utils import load_stock_data

app = FastAPI()

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model + scaler
model = tf.keras.models.load_model("backend/saved_model/lstm_model.h5", compile=False)
scaler = joblib.load("backend/saved_model/scaler.pkl")

class PredictRequest(BaseModel):
    symbol: str

@app.post("/predict")
def predict_price(req: PredictRequest):
    df = load_stock_data(req.symbol, period="1y")
    data = df["Close"].values.reshape(-1, 1)

    last_60 = data[-60:]
    scaled_last_60 = scaler.transform(last_60)

    future_predictions_scaled = []
    current_sequence = scaled_last_60.copy()

    # Predict next 30 days
    for _ in range(30):
        X_input = current_sequence.reshape(1, 60, 1)
        next_scaled = model.predict(X_input)[0][0]

        future_predictions_scaled.append(next_scaled)

        # Update rolling window
        current_sequence = np.append(current_sequence[1:], [[next_scaled]], axis=0)

    # Convert predictions back to real prices
    future_predictions = scaler.inverse_transform(
        np.array(future_predictions_scaled).reshape(-1, 1)
    ).flatten()

    # Prepare historical last 60 days for chart
    historical = data[-60:].flatten().tolist()

    return {
        "symbol": req.symbol,
        "historical_prices": historical,
        "predicted_prices": future_predictions.tolist()
    }
