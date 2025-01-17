from sqlalchemy import Column, String

from src.app.domain.repositories import AuthorRepositoty
from src.app.infrastructure.db.sa_engine import Base
from src.app.infrastructure.db.library import (
    SaAbstactRepositiory, SaAbstractTable
)


class SaAuthorTable(SaAbstractTable, Base):
    __tablename__ = 'author'

    name = Column(String(length=255), nullable=False)


class SaAuthorRepository(SaAbstactRepositiory, AuthorRepositoty):
    ...
