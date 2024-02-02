""" database.py """
from typing import (
    Optional,
    AsyncIterator,
)
import contextlib
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    AsyncConnection,
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.exc import SQLAlchemyError

# from .config import (
#     ASYNC_ENGINE,
#     HOST,
#     PORT,
#     NAME,
#     USERNAME,
#     PASSWORD,
# )
from .base_entity import Base


class DataBaseSessionManager:
    """DataBase Session Manager

    Reference:
        https://praciano.com.br/fastapi-and-async-sqlalchemy-20-with-pytest-done-right.html
    """

    def __init__(self):
        self._engine: Optional[AsyncEngine] = None
        self._sessionmaker: Optional[async_sessionmaker] = None

    def init(self, host: str):
        self._engine = create_async_engine(host, echo=True)
        self._sessionmaker = async_sessionmaker(
            bind=self._engine,
            class_=AsyncSession,
            autocommit=False,
            autoflush=False,
        )

    async def close(self):
        if self._engine is None:
            raise Exception("DataBaseSessionManager is not initalized.")
        await self._engine.dispose()
        self._engine = None
        self._sessionmaker = None

    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self._engine is None:
            raise Exception("DataBaseSessionManager is not initialized.")
        async with self._engine.begin() as conn:
            try:
                yield conn
            except SQLAlchemyError as e:
                await conn.rollback()
                print(f"connect error msg: {e}")

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._sessionmaker is None:
            raise Exception("DataBaseSessionManager is not initialized.")
        session = self._sessionmaker()
        try:
            yield session
        except SQLAlchemyError as e:
            await session.rollback()
            print(f"session error msg: {e}")
        finally:
            await session.close()

    async def create_all(self, conn: AsyncConnection):
        """Used for testing"""
        await conn.run_sync(Base.metadata.create_all)

    async def drop_all(self, conn: AsyncConnection):
        """Used for testing"""
        await conn.run_sync(Base.metadata.drop_all)


sessionmanager = DataBaseSessionManager()


async def get_async_db():
    async with sessionmanager.session() as session:
        yield session
