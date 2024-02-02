"""with_mock.py"""
from typing import Optional
from src.storage.rdb.base_repository import Repository
from src.storage.rdb.user.user_entity import UserEntity
from src.storage.rdb.plate.plate_entity import PlateEntity


class MockUserRepository(Repository[UserEntity]):
    def __init__(self, users: Optional[dict[int, UserEntity]] = None):
        self.users = users or {}

    async def find_by_id(self, id: int) -> Optional[UserEntity]:
        return self.users[id]

    async def find_all(self) -> list[UserEntity]:
        return list(self.users.values())

    async def save(self, t: UserEntity) -> int:
        id = len(self.users)
        self.users[id] = t
        return id

    async def delete_by_id(self, id: int) -> int:
        if self.users.get(id) is None:
            raise Exception("Fail to delete.")

        del self.users[id]
        return id

    async def count(self) -> int:
        return len(self.users)

    async def exists_by_id(self, id: int) -> bool:
        val = self.users.get(id)
        return val is not None


class MockPlateRepository(Repository[PlateEntity]):
    def __init__(self, plates: Optional[dict[int, PlateEntity]] = None):
        self.plates = plates or {}

    async def find_by_id(self, id: int) -> Optional[PlateEntity]:
        return self.plates[id]

    async def find_all(self) -> list[PlateEntity]:
        return list(self.plates.values())

    async def save(self, t: PlateEntity) -> int:
        id = len(self.plates)
        self.plates[id] = t
        return id

    async def delete_by_id(self, id: int) -> int:
        if self.plates.get(id) is None:
            raise Exception("Fail to delete.")

        del self.plates[id]
        return id

    async def count(self) -> int:
        return len(self.plates)

    async def exists_by_id(self, id: int) -> bool:
        val = self.plates.get(id)
        return val is not None
