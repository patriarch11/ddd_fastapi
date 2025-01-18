from src.app.domain.entities import Genre
from src.app.domain.units_of_work import GenreUnitOfWork
from src.shared.di import inject


class GenreService:
    @inject
    def __init__(self, uow: GenreUnitOfWork) -> None:
        self._uow = uow

    def create(self, genre: Genre) -> Genre:
        with self._uow as uow:
            genre = uow.genre.add(genre)
            uow.commit()
            return genre
