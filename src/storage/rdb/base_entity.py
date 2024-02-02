""" base_entity.py """
from sqlalchemy.orm import (
    DeclarativeBase,
    mapped_column,
)
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declared_attr


class BaseEntity:
    """Base Entity

    참고사항: PK 설정은 불가
        @declared_attr
        def id(cls):
            return mapped_column(
                primary_key=True,
                autoincrement=True,
            )
    """

    @declared_attr
    def created_at(cls):
        """생성 일시"""
        return mapped_column(
            DateTime,
            nullable=False,
            server_default=func.now(),
        )

    @declared_attr
    def modified_at(cls):
        """수정 일시"""
        return mapped_column(
            DateTime,
            nullable=False,
            server_default=func.now(),
            server_onupdate=func.now(),
        )


class Base(DeclarativeBase, BaseEntity):
    """SqlAlchemy Declarative ORM"""

    pass
