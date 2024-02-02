""" user_repository_impl.py """
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, func
from ..base_repository import Repository
from .user_entity import UserEntity


class UserRepository(Repository[UserEntity]):
    """User Repository"""

    def __init__(self, db: AsyncSession) -> None:
        self.__db = db

    async def find_by_id(self, id: int) -> Optional[UserEntity]:
        return await self.__db.execute(
            select(UserEntity).where(UserEntity.id == id)
        ).scalar_one()

    async def find_all(self) -> list[UserEntity]:
        return await self.__db.scalars(select(UserEntity)).all()

    async def save(self, t: UserEntity) -> int:
        async with self.__db as session:
            session.add(t)
            session.commit()
            await t.id

    async def delete_by_id(self, id: int) -> int:
        res = await self.__db.execute(delete(UserEntity).where(UserEntity.id == id))
        if res.rowcount == 1:
            return id
        else:
            Exception("Fail to delete.")

    async def count(self) -> int:
        return self.__db.scalar(select(func.count()).select_from(UserEntity))

    async def exists_by_id(self, id: int) -> bool:
        return self.__db.execute(
            select(
                func.exists(select(UserEntity.id).where(UserEntity.id == id).limit(1))
            )
        ).scalar_one()
