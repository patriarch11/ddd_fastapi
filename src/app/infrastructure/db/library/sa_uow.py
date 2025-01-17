from typing import Self

from sqlalchemy.orm import sessionmaker, Session

from src.shared.library import AbstractUnitOfWork


class SaAbstractUnitOfWork(AbstractUnitOfWork):
    def __init__(
            self,
            session_factory: sessionmaker) -> None:
        super().__init__()
        self._session_factory: sessionmaker = session_factory

    def __enter__(self) -> Self:
        self._session: Session = self._session_factory()
        return super().__enter__()

    def __exit__(self, *args, **kwargs) -> None:
        super().__exit__(*args, **kwargs)
        self._session.close()

    def commit(self) -> None:
        self._session.commit()

    def rollback(self) -> None:
        self._session.expunge_all()
        self._session.rollback()
