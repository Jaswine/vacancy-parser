from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship, Mapped
from enum import Enum as PyEnum
from sqlalchemy import func

from models.base import AccountStatus
from configs.database_config import base as Base

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

    last_login = Column(DateTime, server_default=func.now())
    last_active = Column(DateTime, server_default=func.now())
    created_at = Column(DateTime, server_default=func.now())

    link_lists = relationship('LinkList', back_populates='account')
    subscribes = relationship('Subscribe', back_populates='account')
    parsing_logs = relationship('ParsingLog', back_populates='account')

    def __repr__(self) -> str:
        return f'<Account(id={self.id}, username={self.username}, email={self.email}>'

    def __str__(self) -> str:
        return f'Account(id={self.id}, username={self.username}, email={self.email})'