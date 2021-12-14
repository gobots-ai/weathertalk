import logging
from fastapi import FastAPI
from model.request import WeatherRequest

app = FastAPI()
logger = logging.getLogger('uvicorn')


@app.get('/')
def home():
    logger.info("GoBots welcome you!")
    return {'info': "GoBots welcome you!" }


@app.post('/weather')
def weather(request: WeatherRequest):
    # TODO
    return {'output': request.text }
