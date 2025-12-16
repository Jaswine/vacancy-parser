from datetime import datetime

from sqlalchemy import Integer, ForeignKey, String, Enum, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import func

from src.core.db.enums.subscribe_status import ActivitySubscribeStatus
from src.core.db.enums.subscribe_target_type import TargetType
from src.core.db.models.base import Base


class Subscribe(Base):
    """
    Subscribe model
    """

    __tablename__ = "subscribes"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    target_type: Mapped[TargetType] = mapped_column(Enum(TargetType), nullable=False)
    activity_status: Mapped[ActivitySubscribeStatus] = mapped_column(
        Enum(ActivitySubscribeStatus), nullable=False
    )
    end_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("accounts.id"))
    account = relationship(
        "Account", back_populates="subscribes", foreign_keys=[account_id]
    )

    def __repr__(self) -> str:
        return (
            f"<Subscribe(id={self.id}, account_id={self.account_id}, name={self.name}, "
            f"target_type={self.target_type}, activity_status={self.activity_status})>"
        )

    def __str__(self) -> str:
        return (
            f"Subscribe(id={self.id}, account_id={self.account_id}, name={self.name}, "
            f"target_type={self.target_type}, activity_status={self.activity_status})"
        )
