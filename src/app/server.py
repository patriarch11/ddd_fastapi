from contextlib import contextmanager
from typing import Generator

from fastapi import FastAPI
from sqlalchemy.orm import clear_mappers

from src.app.application.handlers import (
    author_handlers, book_handlers, genre_handlers
)
from src.app.infrastructure.db import register_mappers


@contextmanager
def lifespan(_app: FastAPI) -> Generator:
    # register_mappers()
    yield
    clear_mappers()


register_mappers()
app = FastAPI()
app.include_router(author_handlers.router)
app.include_router(book_handlers.router)
app.include_router(genre_handlers.router)
