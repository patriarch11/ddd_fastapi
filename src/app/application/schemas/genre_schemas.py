from pydantic import BaseModel

from src.shared.library import AbstractEntitySchema


class GenreCreateRequest(BaseModel):
    name: str


class GenreSchema(AbstractEntitySchema, GenreCreateRequest):
    ...
