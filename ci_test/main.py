"""
    Main
"""

from fastapi import FastAPI
from pydantic import BaseModel

from .settings import settings

app = FastAPI()


class Status(BaseModel):
    """ Statuc class """
    status: str = "ok"


@app.get(settings.main_url)
async def status():
    """ Status endpoint """
    return Status()
