from dataclasses import dataclass
from src.shared.library import AbstractEntity


@dataclass
class Book(AbstractEntity):
    name: str
    author_id: int
    genre_id: int
