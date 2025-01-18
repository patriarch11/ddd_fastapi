from sqlalchemy.orm import sessionmaker

from src.app.domain.units_of_work import (
    AuthorUnitOfWork, BookUnitOfWork, GenreUnitOfWork
)
from src.app.domain.repositories import (
    AuthorRepository, BookRepository, GenreRepository
)
from src.app.infrastructure.db import (
    SaAuthorUnitOfWork, SaBookUnitOfWork, SaGenreUnitOfWork,
    SaAuthorRepository, SaBookRepository, SaGenreRepository,
    SessionLocal
)
from src.shared.di import Binder, Module, Injector, singleton


class AppModule(Module):
    def configure(self, binder: Binder):
        binder.bind(sessionmaker, SessionLocal, scope=singleton)
        binder.bind(AuthorUnitOfWork, SaAuthorUnitOfWork)
        binder.bind(BookUnitOfWork, SaBookUnitOfWork)
        binder.bind(GenreUnitOfWork, SaGenreUnitOfWork)
        binder.bind(AuthorRepository, SaAuthorRepository)
        binder.bind(BookRepository, SaBookRepository)
        binder.bind(GenreRepository, SaGenreRepository)


injector = Injector([AppModule])
