from sqlalchemy import Column, Integer, ForeignKey, String, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import func

from models.base import Base, ActivityStatus


class Link(Base):
    """
        Link model
    """
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True, index=True)
    link_list_id = Column(Integer, ForeignKey('link_lists.id'))
    company_name = Column(String(255), nullable=True)
    url = Column(String(1500), nullable=False, index=True)
    activity_status = Column(Enum(ActivityStatus), default=ActivityStatus.ACTIVE)

    updated_at = Column(DateTime, server_default=func.now())
    created_at = Column(DateTime, server_default=func.now())

    link_list = relationship('LinkList', back_populates='links', foreign_keys=[link_list_id])


    def __repr__(self) -> str:
        return (f'<Link(id={self.id}, link_list_id={self.link_list_id}, '
                f'company_name={self.company_name}, url={self.url})>')

    def __str__(self) -> str:
        return (f'Link(id={self.id}, link_list_id={self.link_list_id}, '
                f'company_name={self.company_name}, url={self.url})>')
