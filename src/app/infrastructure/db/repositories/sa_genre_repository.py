from sqlalchemy import Column, String, insert, select

from src.app.domain.entities import Genre
from src.app.domain.repositories import GenreRepository
from src.app.infrastructure.db.sa_engine import Base
from src.app.infrastructure.db.library import (
    SaAbstactRepositiory, SaAbstractTable
)
from src.shared.di import singleton


@singleton
class SaGenreTable(Base, SaAbstractTable):
    __tablename__ = 'genre'

    name = Column(String, nullable=False)


@singleton
class SaGenreRepository(SaAbstactRepositiory, GenreRepository):

    def add(self, genre: Genre) -> Genre:
        result = self._session.execute(
            insert(Genre)
            .values(genre.to_dict(exclude={'id'}))
            .returning(Genre)
        )
        return result.scalar_one()

    def update(self, id: int, genre: Genre) -> Genre:
        raise NotImplementedError

    def get(self, id: int) -> Genre | None:
        return self._session.execute(
            select(Genre).filter_by(id=id)
        ).scalar_one_or_none()

    def list(self) -> list[Genre]:
        return list(self._session.execute(select(Genre)).scalars())

    def delete(self, id: int) -> None:
        raise NotImplementedError
