from abc import ABC, abstractmethod

from typing import Generic, TypeVar

TEntity = TypeVar('TEntity')


class AbstractRepository(Generic[TEntity], ABC):

    @abstractmethod
    def add(self, model: TEntity) -> TEntity:
        raise NotImplementedError

    @abstractmethod
    def get(self, id: int) -> TEntity | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, id: int, model: TEntity) -> TEntity:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[TEntity]:
        raise NotImplementedError
