from sqlalchemy import Column, Integer, ForeignKey, relationship, DateTime, String, Boolean
from sqlalchemy import func

from src.models.base import Base

class Filter(Base):
    """
        Filter model
    """
    __tablename__ = 'filters'

    id = Column(Integer, primary_key=True, index=True)
    link_list_id = Column(Integer, ForeignKey('link_lists.id'), index=True)

    title = Column(String(255), default='', nullable=True)
    skills = Column(String(255), default='', nullable=True)
    match_of_skills = Column(Boolean, default=False)
    location = Column(String(255), default='', nullable=True)
    type = Column(String(255), default='', nullable=True)   # Office, Hybrid, Remote, etc.
    salary_range_min = Column(Integer, default=0, nullable=True)
    salary_range_max= Column(Integer, default=0, nullable=True)
    employment_type = Column(String(255), default='', nullable=True)  # Full day, Part time, Contract, Internship, etc.
    experience_level = Column(String(255), default='', nullable=True) # Intern, Junior, Mid, Senior, etc.
    posted_at = Column(DateTime, default=None, nullable=True)
    active_status = Column(String(255), default=True, nullable=True) # Active, Archived, etc.
    created_time = Column(DateTime, default=None, nullable=True)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())

    link_list = relationship('LinkList', back_populates='filters', foreign_keys=[link_list_id])

    def __repr__(self) -> str:
        return f'<Filter(id={self.id}, title={self.title}, link_list_id={self.link_list_id})>'

    def __str__(self) -> str:
        return f'Filter(id={self.id}, title={self.title}, link_list_id={self.link_list_id})'