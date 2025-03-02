from src.models.base import Base
from sqlalchemy import Column, Integer, ForeignKey, String
from enum import Enum as PyEnum, Enum


class LinkListStatus(PyEnum):
    ACTIVE = 'ADMIN'
    HIDDEN = 'HIDDEN'
    ARCHIVED = 'SIMPLE'


class LinkList(Base):
    """
        LinkList model
    """
    __tablename__ = 'link_lists'

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    status = Column(Enum(LinkListStatus), default=LinkListStatus.ADMIN)