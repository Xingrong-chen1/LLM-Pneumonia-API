import os

API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", 8000))

MODEL_PATH = "backend/model/cnn_pneumonia.keras"
