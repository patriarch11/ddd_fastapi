from abc import ABC

from sqlalchemy.orm import Session

from src.shared.library import AbstractRepository


class SaAbstactRepositiory(AbstractRepository, ABC):
    def __init__(self, session: Session) -> None:
        self._session = session
