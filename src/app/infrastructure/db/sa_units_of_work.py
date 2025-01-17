from typing import Self

from src.app.domain.repositories import BookRepository
from src.app.domain.units_of_work import BookUnitOfWork

from .library import SaAbstractUnitOfWork
from .repositories import SaBookRepository


class SaBookUnitOfWork(SaAbstractUnitOfWork, BookUnitOfWork):
    def __enter__(self) -> Self:
        uow = super().__enter__()
        self.book: BookRepository = SaBookRepository(session=self._session)
        return uow
