from pydantic import BaseModel

class WeatherRequest(BaseModel):
    text: str
