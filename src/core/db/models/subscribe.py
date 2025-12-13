from sqlalchemy import Column, Integer, ForeignKey, String, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import func

from src.core.db.enums.subscribe_status import ActivitySubscribeStatus
from src.core.db.enums.subscribe_target_type import TargetType
from src.core.db.models.base import BaseModel


class Subscribe(BaseModel):
    """
        Subscribe model
    """
    __tablename__ = 'subscribes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    target_type = Column(Enum(TargetType), default=TargetType.MONTHLY, nullable=True)
    activity_status = Column(Enum(ActivitySubscribeStatus), nullable=True)
    end_at = Column(DateTime, server_default=func.now())

    account_id = Column(Integer, ForeignKey('accounts.id'))
    account = relationship('Account', back_populates='subscribes', foreign_keys=[account_id])

    def __repr__(self) -> str:
        return (f'<Subscribe(id={self.id}, account_id={self.account_id}, name={self.name}, '
                f'target_type={self.target_type}, activity_status={self.activity_status})>')

    def __str__(self) -> str:
        return (f'Subscribe(id={self.id}, account_id={self.account_id}, name={self.name}, '
                f'target_type={self.target_type}, activity_status={self.activity_status})')