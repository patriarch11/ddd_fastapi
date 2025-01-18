from fastapi import APIRouter, Depends

from src.app.application.schemas import GenreCreateRequest, GenreSchema
from src.app.di import injector
from src.app.domain.entities import Genre
from src.app.domain.services import GenreService

router = APIRouter(prefix='/genre')


def get_service() -> GenreService:
    return injector.get(GenreService)


@router.post('/create')
def create(
    request: GenreCreateRequest,
    service: GenreService = Depends(get_service)
) -> GenreSchema:
    author = service.create(Genre(**request.model_dump()))
    return GenreSchema(**author.to_dict())
