from src.app.domain.entities import Author, Book, Genre

from .sa_engine import mapper_registry
from sqlalchemy.orm import class_mapper
from sqlalchemy.orm.exc import UnmappedClassError

from src.app.infrastructure.db.repositories import (
    SaAuthorTable, SaBookTable, SaGenreTable
)


def register_mappers():
    mapper_registry.map_imperatively(SaAuthorTable, local_table=Author)
    mapper_registry.map_imperatively(SaBookTable, local_table=Book)
    mapper_registry.map_imperatively(SaGenreTable, local_table=Genre)
