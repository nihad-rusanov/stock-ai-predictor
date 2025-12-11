# 📈 stock-ai-predictor  
AI Stock Price Forecasting Web Application

A modern, visually engaging web application that predicts **30-day future stock prices** using a trained **LSTM neural network**.

The platform features a beautifully designed frontend, a high-performance FastAPI backend, and clear, interactive visualizations of both historical and forecasted stock trends.

---

## ✨ Features

### **1. Modern Web Interface**
- Clean, animated UI with glass-morphism design  
- Input for any market symbol (AAPL, TSLA, BTC-USD, etc.)  
- Beautiful combined chart of **60-day historical** + **30-day predicted** prices  
- Smooth transitions, gradients, and responsive layout  

---

### **2. Deep Learning Forecasting**
- LSTM model trained on historical closing prices  
- Autoregressive loop generates **1-month future prediction**  
- Scaled and inverse-scaled outputs using MinMaxScaler  
- Fast inference powered by TensorFlow + FastAPI  

---

### **3. Full-Stack Architecture**
stock-forecast-app/
│
├── backend/
│ ├── main.py # FastAPI server
│ ├── utils.py # Data loading + preprocess
│ ├── train_model.py # Model training script
│ ├── saved_model/
│ │ ├── lstm_model.h5
│ │ └── scaler.pkl
│ └── requirements.txt
│
└── frontend/
├── index.html # Web interface
├── script.js # Fetch + chart logic
└── styles.css # UI styling


---

## 🧠 How the Prediction Works

1. Fetch last **60 days** of closing prices from Yahoo Finance  
2. Normalize prices using a fitted MinMaxScaler  
3. Model predicts the next day’s price  
4. Append prediction → repeat for **30 cycles**  
5. Convert predicted values back to real prices  
6. Frontend renders a seamless chart of past & future  

---

## 🚀 Running the Backend Locally

### **1. Install dependencies**
```bash
pip install -r backend/requirements.txt

2. Train the model (run once)
python backend/train_model.py


This generates:

backend/saved_model/lstm_model.h5
backend/saved_model/scaler.pkl

3. Start the FastAPI server
uvicorn backend.main:app --reload


Backend will run at:

http://127.0.0.1:8000

💻 Running the Frontend Locally

Open:

frontend/index.html


Ensure your script.js uses your local backend:

fetch("http://127.0.0.1:8000/predict", { ... });

🌐 Deployment Guide
Backend Deployment (Render)

Push your project to GitHub

Add render.yaml in the project root:

services:
  - type: web
    name: stock-ai-backend
    env: python
    buildCommand: "pip install -r backend/requirements.txt"
    startCommand: "uvicorn backend.main:app --host 0.0.0.0 --port $PORT"


Go to Render → New Web Service → Select your repository

Deploy

Copy your backend URL:

https://your-backend.onrender.com

Frontend Deployment (Netlify or Vercel)

Go to Netlify

Upload only your frontend folder

Update API URL in script.js:

fetch("https://your-backend.onrender.com/predict", { ... });


Your app is now publicly available worldwide.

🔎 Example Stock Symbols to Test
AAPL
MSFT
AMZN
NVDA
TSLA
META
GOOGL
BTC-USD
ETH-USD
SPY
QQQ

🛠 Future Improvements (Roadmap)

Transformer-based forecasting

Multi-stock comparison mode

Candlestick chart with future overlay

Real-time live data updates

Confidence interval visualization

User accounts and saved watchlists

📜 License

MIT License

✍️ Author

Nihat
For learning, forecasting, and financial data visualization.








