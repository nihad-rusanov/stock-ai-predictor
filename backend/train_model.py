from utils import load_stock_data, prepare_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import numpy as np
import joblib
import os

# Load stock data
df = load_stock_data("AAPL")
X, y, scaler = prepare_sequences(df.values)

# Reshape for LSTM
X = X.reshape((X.shape[0], X.shape[1], 1))

# Build LSTM model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)),
    Dropout(0.2),
    LSTM(50),
    Dropout(0.2),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')

# Train
model.fit(X, y, epochs=3, batch_size=32)

# Create output folder if not exists
os.makedirs("backend/saved_model", exist_ok=True)

# Save the trained model
model.save("backend/saved_model/lstm_model.h5")

# Save the fitted scaler
joblib.dump(scaler, "backend/saved_model/scaler.pkl")

print("Training complete. Model + scaler saved.")
