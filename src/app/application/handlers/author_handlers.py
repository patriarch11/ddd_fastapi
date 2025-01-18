from fastapi import APIRouter, Depends

from src.app.application.schemas import AuthorCreateRequest, AuthorSchema
from src.app.di import injector
from src.app.domain.entities import Author
from src.app.domain.services import AuthorService

router = APIRouter(prefix='/author')


def get_service() -> AuthorService:
    return injector.get(AuthorService)


@router.post('/create')
def create(
    request: AuthorCreateRequest,
    service: AuthorService = Depends(get_service)
) -> AuthorSchema:
    author = service.create(Author(
        id=None, created_at=None, updated_at=None,
        full_name=request.full_name
    ))
    return AuthorSchema(**author.to_dict())
