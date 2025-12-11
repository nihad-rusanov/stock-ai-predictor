import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import yfinance as yf

# Scaler will be loaded later (not created here)
scaler = None

def load_stock_data(symbol="AAPL", period="5y"):
    df = yf.download(symbol, period=period)
    df = df[['Close']]
    return df

def prepare_sequences(data, window=60):
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(data)

    X, y = [], []

    for i in range(window, len(scaled)):
        X.append(scaled[i-window:i, 0])
        y.append(scaled[i, 0])

    return np.array(X), np.array(y), scaler
