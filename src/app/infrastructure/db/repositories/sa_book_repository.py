from sqlalchemy import Column, String, ForeignKey, Integer


from src.app.domain.entities import Book
from src.app.domain.repositories import BookRepository
from src.app.infrastructure.db.sa_engine import Base
from src.app.infrastructure.db.library import (
    SaAbstactRepositiory, SaAbstractTable
)


class SaBookTable(Base, SaAbstractTable):
    __tablename__ = 'book'

    author_id = Column(Integer, ForeignKey('author.id'))
    genre_id = Column(Integer, ForeignKey('genre.id'))
    name = Column(String, nullable=False)


class SaBookRepository(SaAbstactRepositiory, BookRepository):
    def add(self, model: Book) -> Book:
        ...

    def update(self, id: int, model: Book) -> Book:
        ...

    def get(self, id: int) -> Book:
        ...

    def list(self) -> list[Book]:
        ...

    def delete(self, id: int) -> None:
        ...
