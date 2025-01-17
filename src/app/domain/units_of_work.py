from abc import ABC

from src.shared.library import AbstractUnitOfWork

from .repositories import BookRepository


class BookUnitOfWork(AbstractUnitOfWork, ABC):
    book: BookRepository
