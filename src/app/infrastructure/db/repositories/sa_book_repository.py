from sqlalchemy import (
    Column, String, ForeignKey, Integer, insert, select, update
)

from src.app.domain.entities import Book
from src.app.domain.repositories import BookRepository
from src.app.infrastructure.db.sa_engine import Base
from src.app.infrastructure.db.library import (
    SaAbstactRepositiory, SaAbstractTable
)
from src.shared.di import singleton


@singleton
class SaBookTable(Base, SaAbstractTable):
    __tablename__ = 'book'

    author_id = Column(Integer, ForeignKey('author.id'))
    genre_id = Column(Integer, ForeignKey('genre.id'))
    name = Column(String, nullable=False)


class SaBookRepository(SaAbstactRepositiory, BookRepository):
    def add(self, book: Book) -> Book:
        return self._session.execute(
            insert(Book)
            .values(book.to_dict(exclude={'id'}))
            .returning(Book)
        ).scalar_one()

    def update(self, id: int, book: Book) -> Book:
        return self._session.execute(
            update(Book).filter_by(id=id)
            .values(book.to_dict(exclude={'id'}))
            .returning(Book)
        ).scalar_one()

    def get(self, id: int) -> Book | None:
        return self._session.execute(
            select(Book).filter_by(id=id)
        ).scalar_one_or_none()

    def list(self) -> list[Book]:
        return list(self._session.execute(select(Book)).scalars())

    def delete(self, id: int) -> None:
        raise NotImplementedError
