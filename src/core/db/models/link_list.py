from sqlalchemy import Column, Integer, ForeignKey, String, Enum, DateTime
from sqlalchemy.orm import relationship

from src.core.db.enums.status import Status
from src.core.db.models.base import BaseModel


class LinkList(BaseModel):
    """
        LinkList model
    """
    __tablename__ = 'link_lists'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    activity_status = Column(Enum(Status), default=Status.ACTIVE)

    account_id = Column(Integer, ForeignKey("accounts.id"))
    account = relationship('Account', back_populates='link_lists', foreign_keys=[account_id])

    links = relationship('Link', back_populates='link_list')
    parsing_logs = relationship('ParsingLog', back_populates='link_list')
    filters = relationship('Filter', back_populates='link_list')

    def __repr__(self) -> str:
        return f'<LinkList(id={self.id}, name={self.name}, activity_status={self.activity_status})>'

    def __str__(self) -> str:
        return f'LinkList(id={self.id}, name={self.name}, activity_status={self.activity_status})'
