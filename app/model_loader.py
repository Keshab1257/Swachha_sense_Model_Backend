import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

model_path = os.path.join(BASE_DIR, "model", "swachsense_model.pkl")
scaler_path = os.path.join(BASE_DIR, "model", "gas_scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)