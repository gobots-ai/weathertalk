import logging
from fastapi import FastAPI

app = FastAPI()
logger = logging.getLogger('uvicorn')


@app.get('/')
def home():
    logger.info("GoBots welcome you!")
    return {'info': "GoBots welcome you!" }
