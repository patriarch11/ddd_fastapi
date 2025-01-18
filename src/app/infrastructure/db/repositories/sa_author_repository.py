from sqlalchemy import Column, String, insert, select

from src.app.domain.entities import Author
from src.app.domain.repositories import AuthorRepository
from src.app.infrastructure.db.sa_engine import Base
from src.app.infrastructure.db.library import (
    SaAbstactRepositiory, SaAbstractTable
)
from src.shared.di import singleton


@singleton
class SaAuthorTable(SaAbstractTable, Base):
    __tablename__ = 'author'

    full_name = Column(String(length=255), nullable=False)


class SaAuthorRepository(SaAbstactRepositiory, AuthorRepository):

    def add(self, author: Author) -> Author:
        result = self._session.execute(
            insert(Author)
            .values(author.to_dict(exclude={'id'}))
            .returning(Author)
        )
        return result.scalar_one()

    def update(self, id: int, author: Author) -> Author:
        raise NotImplementedError

    def get(self, id: int) -> Author | None:
        return self._session.execute(
            select(Author).filter_by(id=id)
        ).scalar_one_or_none()

    def list(self) -> list[Author]:
        return list(self._session.execute(select(Author)).scalars())

    def delete(self, id: int) -> None:
        raise NotImplementedError
