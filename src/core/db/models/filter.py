from sqlalchemy import Column, Integer, ForeignKey, DateTime, String, Boolean, Enum
from sqlalchemy.orm import relationship

from src.core.db.enums.filter_employment_type import FilterEmploymentType
from src.core.db.enums.filter_experience_level import FilterExperienceLevel
from src.core.db.enums.filter_work_type import FilterWorkType
from src.core.db.enums.status import Status
from src.core.db.models.base import BaseModel


class Filter(BaseModel):
    """
        Filter model
    """
    __tablename__ = 'filters'

    title = Column(String(255), default='', nullable=True)
    skills = Column(String(255), default='', nullable=True)
    match_of_skills = Column(Boolean, default=False)
    location = Column(String(255), default='', nullable=True)
    work_type = Column(Enum(FilterWorkType), default=FilterWorkType.OFFICE, nullable=True)   # Office, Hybrid, Remote, etc.
    salary_range_min = Column(Integer, default=0, nullable=True)
    salary_range_max= Column(Integer, default=0, nullable=True)
    employment_type = Column(Enum(FilterEmploymentType), default=FilterEmploymentType.FULL_TIME, nullable=True)  # Full time, Part time, Contract, Internship, etc.
    experience_level = Column(Enum(FilterExperienceLevel), default='', nullable=True) # Intern, Junior, Mid, Senior, etc.
    posted_at = Column(DateTime, default=None, nullable=True)  # When it was posted public
    active_status = Column(Enum(Status), default=Status.ACTIVE, nullable=True) # Active, Archived, etc.
    created_time = Column(DateTime, default=None, nullable=True)

    link_list_id = Column(Integer, ForeignKey('link_lists.id'), index=True)
    link_list = relationship('LinkList', back_populates='filters', foreign_keys=[link_list_id])

    def __repr__(self) -> str:
        return f'<Filter(id={self.id}, title={self.title}, link_list_id={self.link_list_id})>'

    def __str__(self) -> str:
        return f'Filter(id={self.id}, title={self.title}, link_list_id={self.link_list_id})'