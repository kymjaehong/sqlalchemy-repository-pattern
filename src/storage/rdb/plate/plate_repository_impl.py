""" plate_repository_impl.py """
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, func
from ..base_repository import Repository
from .plate_entity import PlateEntity


class PlateRepository(Repository[PlateEntity]):
    """Plate Repository"""

    def __init__(self, db: AsyncSession) -> None:
        self.__db = db

    async def find_by_id(self, id: int) -> Optional[PlateEntity]:
        return await self.__db.execute(
            select(PlateEntity).where(PlateEntity.id == id)
        ).scalar_one()

    async def find_all(self) -> list[PlateEntity]:
        return await self.__db.scalars(select(PlateEntity)).all()

    async def save(self, t: PlateEntity) -> int:
        async with self.__db as session:
            session.add(t)
            session.commit()
            await t.id

    async def delete_by_id(self, id: int) -> int:
        res = await self.__db.execute(delete(PlateEntity).where(PlateEntity.id == id))
        if res.rowcount == 1:
            return id
        else:
            Exception("Fail to delete.")

    async def count(self) -> int:
        return self.__db.scalar(select(func.count()).select_from(PlateEntity))

    async def exists_by_id(self, id: int) -> bool:
        return await self.__db.execute(
            select(
                func.exists(select(PlateEntity.id).where(PlateEntity.id == id).limit(1))
            )
        ).scalar_one()
