from sqlalchemy import Column, String


from src.app.domain.repositories import GenreRepositoty
from src.app.infrastructure.db.sa_engine import Base
from src.app.infrastructure.db.library import (
    SaAbstactRepositiory, SaAbstractTable
)


class SaGenreTable(Base, SaAbstractTable):
    __tablename__ = 'genre'

    name = Column(String, nullable=False)


class SaGenreRepository(SaAbstactRepositiory, GenreRepositoty):
    ...
