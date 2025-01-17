from abc import ABC

from src.app.domain.entities import Genre
from src.shared.library import AbstractRepository


class GenreRepositoty(AbstractRepository[Genre], ABC):
    ...
