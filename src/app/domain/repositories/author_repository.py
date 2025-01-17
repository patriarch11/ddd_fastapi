from abc import ABC

from src.app.domain.entities import Author
from src.shared.library import AbstractRepository


class AuthorRepositoty(AbstractRepository[Author], ABC):
    ...
