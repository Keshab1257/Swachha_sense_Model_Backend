import joblib
import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

model_path = os.path.join(BASE_DIR, "model", "swachsense_model.pkl")
scaler_path = os.path.join(BASE_DIR, "model", "gas_scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)


def predict_hygiene_state(mq35, mq36, temperature, humidity):

    # normalize gases
    norm_values = scaler.transform([[mq35, mq36]])
    mq35_norm, mq36_norm = norm_values[0]

    # gas ratio
    gas_ratio = mq35 / (mq36 + 1e-6)

    features = np.array([[
        mq35_norm,
        mq36_norm,
        gas_ratio,
        temperature,
        humidity
    ]])

    prediction = model.predict(features)[0]

    return prediction

state = predict_hygiene_state(
    mq35=135,
    mq36=110,
    temperature=36,
    humidity=40
)

print("Predicted Hygiene State:", state)