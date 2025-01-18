from typing import Self

from src.app.domain.repositories import (
    AuthorRepository, BookRepository, GenreRepository
)
from src.app.domain.units_of_work import (
    AuthorUnitOfWork, BookUnitOfWork, GenreUnitOfWork
)


from .library import SaAbstractUnitOfWork
from .repositories import (
    SaAuthorRepository, SaBookRepository, SaGenreRepository
)


class SaAuthorUnitOfWork(SaAbstractUnitOfWork, AuthorUnitOfWork):
    def __enter__(self) -> Self:
        uow = super().__enter__()
        self.author: AuthorRepository = SaAuthorRepository(self._session)
        return uow


class SaBookUnitOfWork(SaAbstractUnitOfWork, BookUnitOfWork):
    def __enter__(self) -> Self:
        uow = super().__enter__()
        self.author: AuthorRepository = SaAuthorRepository(self._session)
        self.book: BookRepository = SaBookRepository(self._session)
        self.genre: GenreRepository = SaGenreRepository(self._session)
        return uow


class SaGenreUnitOfWork(SaAbstractUnitOfWork, GenreUnitOfWork):
    def __enter__(self) -> Self:
        uow = super().__enter__()
        self.author: GenreRepository = SaGenreRepository(self._session)
        return uow
