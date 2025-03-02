from sqlalchemy import Column, Integer, ForeignKey, String, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import func
from enum import Enum as PyEnum

from models.base import Base, ActivityStatus

class TargetType(PyEnum):
    MONTHLY = 'MONTHLY'
    YEARLY = 'YEARLY'

class ActivitySubscribeStatus(PyEnum):
    ACTIVE = 'ACTIVE'
    BLOCKED = 'BLOCKED'
    ARCHIVED = 'ARCHIVED'
    DISABLED = 'DISABLED'
    FAILED = 'FAILED'
    PENDING = 'PENDING'
    SUSPENDED = 'SUSPENDED'


class Subscribe(Base):
    """
        Subscribe model
    """
    __tablename__ = 'subscribes'

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    name = Column(String(255), nullable=False)
    target_type = Column(Enum(TargetType), default=TargetType.MONTHLY)
    activity_status = Column(Enum(ActivityStatus), default=ActivitySubscribeStatus.PENDING)

    end_at = Column(DateTime, server_default=func.now())
    created_at = Column(DateTime, server_default=func.now())
    last_activity = Column(DateTime, server_default=func.now())

    account = relationship('Account', back_populates='accounts', foreign_keys=[account_id])

    def __repr__(self) -> str:
        return (f'<Subscribe(id={self.id}, account_id={self.account_id}, name={self.name}, '
                f'target_type={self.target_type}, activity_status={self.activity_status})>')

    def __str__(self) -> str:
        return (f'Subscribe(id={self.id}, account_id={self.account_id}, name={self.name}, '
                f'target_type={self.target_type}, activity_status={self.activity_status})')