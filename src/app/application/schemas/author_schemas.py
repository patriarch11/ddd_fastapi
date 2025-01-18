from pydantic import BaseModel

from src.shared.library import AbstractEntitySchema


class AuthorCreateRequest(BaseModel):
    full_name: str


class AuthorSchema(AbstractEntitySchema, AuthorCreateRequest):
    ...
