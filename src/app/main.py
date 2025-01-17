from contextlib import contextmanager
from typing import Generator

from fastapi import FastAPI
from sqlalchemy.orm import clear_mappers

from src.app.infrastructure.db import register_mappers


app = FastAPI()


@contextmanager
def lifespan(_app: FastAPI) -> Generator:
    register_mappers()
    yield
    clear_mappers()
