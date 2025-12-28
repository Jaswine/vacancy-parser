import uuid

from datetime import datetime

from sqlalchemy import Integer, ForeignKey, DateTime, String, Boolean, Enum
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.core.db.enums.filter_employment_type import FilterEmploymentType
from src.core.db.enums.filter_experience_level import FilterExperienceLevel
from src.core.db.enums.filter_work_type import FilterWorkType
from src.core.db.enums.status import Status
from src.core.db.models.base import Base


class Filter(Base):
    """
    Filter model
    """

    __tablename__ = "filters"

    collection_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("collections.id"), index=True
    )

    title: Mapped[str | None] = mapped_column(String(255), default="", nullable=True)
    skills: Mapped[str | None] = mapped_column(String(255), default="", nullable=True)
    complete_match_of_skills: Mapped[bool | None] = mapped_column(
        Boolean, default=False, nullable=True
    )
    location: Mapped[str | None] = mapped_column(String(255), default="", nullable=True)

    work_format: Mapped[FilterWorkType | None] = mapped_column(
        Enum(FilterWorkType), default=FilterWorkType.OFFICE, nullable=True
    )  # Office, Hybrid, Remote, etc.

    salary_range_min: Mapped[int | None] = mapped_column(
        Integer, default=0, nullable=True
    )
    salary_range_max: Mapped[int | None] = mapped_column(
        Integer, default=0, nullable=True
    )

    employment_type: Mapped[FilterEmploymentType | None] = mapped_column(
        Enum(FilterEmploymentType),
        default=FilterEmploymentType.FULL_TIME,
        nullable=True,
    )  # Full time, Part time, Contract, Internship, etc.

    experience_level: Mapped[FilterExperienceLevel | None] = mapped_column(
        Enum(FilterExperienceLevel), default=None, nullable=True
    )  # Intern, Junior, Mid, Senior, etc.

    active_status: Mapped[Status | None] = mapped_column(
        Enum(Status), default=Status.ACTIVE, nullable=True
    )  # Active, Archived, etc.

    posted_at: Mapped[datetime | None] = mapped_column(
        DateTime, default=None, nullable=True
    )  # When it's public

    collection = relationship(
        "Collection", back_populates="filters", foreign_keys=[collection_id]
    )

    def __repr__(self) -> str:
        return (
            f"<Filter(id={self.id}, title={self.title}, "
            f"collection_id={self.collection_id})>"
        )

    def __str__(self) -> str:
        return (
            f"Filter(id={self.id}, title={self.title}, "
            f"collection_id={self.collection_id})"
        )
