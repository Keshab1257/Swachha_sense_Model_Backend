from fastapi import FastAPI, HTTPException
from app.schemas import SensorData
from app.predictor import predict_hygiene

app = FastAPI(
    title="SwachSense API",
    version="1.0"
)

# --------------------------
# Health Check
# --------------------------
@app.get("/")
def home():
    return {"message": "SwachSense API Running"}


# --------------------------
# Prediction Endpoint
# --------------------------
@app.post("/predict")
def predict(data: SensorData):

    try:
        # Basic validation (important for real systems)
        if data.mq35 < 0 or data.mq36 < 0:
            raise ValueError("Gas values cannot be negative")

        result = predict_hygiene(
            data.mq35,
            data.mq36,
            data.temperature,
            data.humidity
        )

        return {
            "prediction": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )