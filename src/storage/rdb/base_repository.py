""" base_repository.py """
from abc import ABC, abstractmethod
from typing import Optional


class Repository[T](ABC):
    """Repository Interface

    Reference:
        https://docs.sqlalchemy.org/en/20/changelog/migration_20.html
        https://docs.spring.io/spring-data/jpa/docs/current/api/org/springframework/data/jpa/repository/JpaRepository.html
    """

    @abstractmethod
    async def find_by_id(self, id: int) -> Optional[T]:
        raise NotImplementedError

    @abstractmethod
    async def find_all(self) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    async def save(self, t: T) -> int:
        raise NotImplementedError

    @abstractmethod
    async def delete_by_id(self, id: int) -> int:
        raise NotImplementedError

    @abstractmethod
    async def count(self) -> int:
        raise NotImplementedError

    @abstractmethod
    async def exists_by_id(self, id: int) -> bool:
        raise NotImplementedError
