from pydantic import BaseModel

from src.shared.library import AbstractEntitySchema


class BookCreateRequest(BaseModel):
    name: str
    genre_id: str
    autor_id: str


class BookSchema(AbstractEntitySchema, BookCreateRequest):
    ...
