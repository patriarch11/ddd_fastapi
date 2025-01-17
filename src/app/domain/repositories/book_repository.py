from abc import ABC

from src.app.domain.entities import Book
from src.shared.library import AbstractRepository


class BookRepository(AbstractRepository[Book], ABC):
    ...
