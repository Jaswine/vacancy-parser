from sqlalchemy import Column, Integer, ForeignKey, String, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import func

from models.base import Base, ActivityStatus


class LinkList(Base):
    """
        LinkList model
    """
    __tablename__ = 'link_lists'

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    name = Column(String(255), nullable=False)
    activity_status = Column(Enum(ActivityStatus), default=ActivityStatus.ACTIVE)

    updated_at = Column(DateTime, server_default=func.now())
    created_at = Column(DateTime, server_default=func.now())

    account = relationship('Account', back_populates='link_lists', foreign_keys=[account_id])

    links = relationship('Link', back_populates='link_list')
    parsing_logs = relationship('ParsingLog', back_populates='link_list')
    filters = relationship('Filter', back_populates='link_list')

    def __repr__(self) -> str:
        return f'<LinkList(id={self.id}, name={self.name}, activity_status={self.activity_status})>'

    def __str__(self) -> str:
        return f'LinkList(id={self.id}, name={self.name}, activity_status={self.activity_status})'
