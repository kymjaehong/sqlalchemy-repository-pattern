""" plate_entity.py """
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from ..base_entity import Base


class PlateEntity(Base):
    """Plate Table"""

    __tablename__ = "plate"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(String, nullable=False)
    is_complete: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    user_id: Mapped[int] = mapped_column(String, nullable=False)

    # 생명주기가 동일하다면, user property 연관관계 설정 (ManyToOne)
