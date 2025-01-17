from src.shared.library import AbstractEntity


class Book(AbstractEntity):
    name: str
    author_id: int
    genre_id: int
