from abc import ABC

from src.shared.library import AbstractUnitOfWork

from .repositories import AuthorRepository, BookRepository, GenreRepository


class AuthorUnitOfWork(AbstractUnitOfWork, ABC):
    author: AuthorRepository


class BookUnitOfWork(AbstractUnitOfWork, ABC):
    author: AuthorRepository
    book: BookRepository
    genre: GenreRepository


class GenreUnitOfWork(AbstractUnitOfWork, ABC):
    genre: GenreRepository
