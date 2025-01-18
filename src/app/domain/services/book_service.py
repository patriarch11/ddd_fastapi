from src.app.domain.entities import Book
from src.app.domain.errors import Error, NotFoundError
from src.app.domain.units_of_work import BookUnitOfWork
from src.shared.di import inject


class BookService:
    @inject
    def __init__(self, uow: BookUnitOfWork) -> None:
        self._uow = uow

    def create(self, book: Book) -> Book:
        with self._uow as uow:
            if (
                not uow.author.get(book.author_id) or
                not uow.genre.get(book.genre_id)
            ):
                raise Error('No such author or genre')
            book = uow.book.add(book)
            uow.commit()
            return book

    def update(self, book: Book) -> Book:
        with self._uow as uow:
            if not uow.book.get(book.id):
                raise NotFoundError('Book not found')
            book = uow.book.update(book.id, book)
            uow.commit()
            return book

    def get(self, id: int) -> Book:
        with self._uow as uow:
            if book := uow.book.get(id):
                return book
            raise NotFoundError('Book not found')

    def get_list(self) -> list[Book]:
        with self._uow as uow:
            return uow.book.list()
