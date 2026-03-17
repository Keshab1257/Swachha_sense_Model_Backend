from pydantic import BaseModel

class SensorData(BaseModel):
    mq35: float
    mq36: float
    temperature: float
    humidity: float