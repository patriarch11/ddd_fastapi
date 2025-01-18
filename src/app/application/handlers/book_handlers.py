from fastapi import APIRouter, Depends

from src.app.application.schemas import BookCreateRequest, BookSchema
from src.app.di import injector
from src.app.domain.entities import Book
from src.app.domain.services import BookService

router = APIRouter(prefix='/book')


def get_service() -> BookService:
    return injector.get(BookService)


@router.post('/create')
def create(
    request: BookCreateRequest,
    service: BookService = Depends(get_service)
) -> BookSchema:
    author = service.create(Book(**request.model_dump()))
    return BookSchema(**author.to_dict())
