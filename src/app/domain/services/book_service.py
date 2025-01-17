from src.app.domain.entities import Book
from src.app.domain.units_of_work import BookUnitOfWork


class BookService:

    def __init__(self, uow: BookUnitOfWork) -> None:
        self._uow = uow

    def create(self, book: Book) -> Book:
        with self._uow as uow:
            book = uow.book.add(book)
            uow.commit()
            return book
