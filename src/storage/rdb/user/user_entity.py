""" user_entity.py """
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from ..base_entity import Base


class UserEntity(Base):
    """User Table"""

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    account_id: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)

    # 광고 수신 여부 등
