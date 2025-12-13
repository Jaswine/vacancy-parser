from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy import func

from src.core.db.enums.status import Status
from src.core.db.enums.account_type import AccountType
from src.core.db.models.base import BaseModel


class Account(BaseModel):
    """
        Account model
    """
    __tablename__ = 'accounts'

    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

    account_status = Column(Enum(Status), default=Status.ACTIVE)
    account_type = Column(Enum(AccountType), default=AccountType.SIMPLE)

    last_login = Column(DateTime, server_default=func.now())
    last_active = Column(DateTime, server_default=func.now())

    link_lists = relationship('LinkList', back_populates='account')
    subscribes = relationship('Subscribe', back_populates='account')
    parsing_logs = relationship('ParsingLog', back_populates='account')

    def __repr__(self) -> str:
        return f'<Account(id={self.id}, username={self.username}, email={self.email}>'

    def __str__(self) -> str:
        return f'Account(id={self.id}, username={self.username}, email={self.email})'