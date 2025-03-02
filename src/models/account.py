from sqlalchemy import Column, Integer, String, DateTime, Enum, relationship
from src.models.base import Base
from enum import Enum as PyEnum
from sqlalchemy import func

class AccountStatus(PyEnum):
    ACTIVE = 'ACTIVE'
    BLOCKED = 'BLOCKED'
    ARCHIVED = 'ARCHIVED'

class AccountType(PyEnum):
    ADMIN = 'ADMIN'
    SIMPLE = 'SIMPLE'

class Account(Base):
    """
        Account model
    """
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

    account_status = Column(Enum(AccountStatus), default=AccountStatus.ACTIVE)
    account_type = Column(Enum(AccountType), default=AccountType.SIMPLE)

    updated_at = Column(DateTime, server_default=func.now())
    created_at = Column(DateTime, server_default=func.now())

    link_lists = relationship('LinkList', back_populates='link_list')

    def __repr__(self) -> str:
        return f'<Account(id={self.id}, username={self.username}, email={self.email}>'

    def __str__(self) -> str:
        return f'Account(id={self.id}, username={self.username}, email={self.email})'