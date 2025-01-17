from src.app.domain.entities import Author, Book, Genre

from .sa_engine import mapper_registry


def register_mappers():
    from src.app.infrastructure.db.repositories import (
        SaAuthorTable, SaBookTable, SaGenreTable
    )
    mapper_registry.map_imperatively(Author, SaAuthorTable)
    mapper_registry.map_imperatively(Book, SaBookTable)
    mapper_registry.map_imperatively(Genre, SaGenreTable)
