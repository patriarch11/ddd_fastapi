from src.app.domain.entities import Author
from src.app.domain.units_of_work import AuthorUnitOfWork
from src.shared.di import inject


class AuthorService:
    @inject
    def __init__(self, uow: AuthorUnitOfWork) -> None:
        self._uow = uow

    def create(self, author: Author) -> Author:
        with self._uow as uow:
            author = uow.author.add(author)
            uow.commit()
            return author
