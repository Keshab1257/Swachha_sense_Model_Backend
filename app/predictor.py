import pandas as pd
from app.model_loader import model, scaler

def predict_hygiene(mq35, mq36, temperature, humidity):

   
    gas_input = pd.DataFrame({
        "mq35": [mq35],
        "mq36": [mq36]
    })

    norm = scaler.transform(gas_input)
    mq35_norm, mq36_norm = norm[0]
 
    gas_ratio = mq35 / (mq36 + 1e-6)
 
    features = pd.DataFrame({
        "mq35_norm": [mq35_norm],
        "mq36_norm": [mq36_norm],
        "gas_ratio": [gas_ratio],
        "temp_C": [temperature],
        "humidity": [humidity]
    })
 
    pred = model.predict(features)[0]

    return pred   