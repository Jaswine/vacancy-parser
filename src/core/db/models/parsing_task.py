from datetime import datetime

from sqlalchemy import Integer, ForeignKey, DateTime, Enum, String, Text
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship, mapped_column, Mapped

from src.core.db.models import ParsingJob, Link
from src.core.db.enums.job_task_status import JobTaskStatus
from src.core.db.models.base import Base


class ParsingTask(Base):
    """
    ParsingTask model
    """

    __tablename__ = "parsing_tasks"

    parsing_job_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("parsing_jobs.id")
    )
    link_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("links.id")
    )
    status: Mapped[JobTaskStatus] = mapped_column(Enum(JobTaskStatus),
                                                  default=JobTaskStatus.PENDING, nullable=False)

    attempts: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    last_error: Mapped[str] = mapped_column(Text, nullable=True)

    started_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    finished_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    parsing_job: Mapped[ParsingJob] = relationship(
        "ParsingJob", back_populates="parsing_tasks", foreign_keys=[parsing_job_id]
    )
    link: Mapped[Link] = relationship(
        "Link", back_populates="parsing_tasks", foreign_keys=[link_id]
    )

    def __repr__(self) -> str:
        return (f"<ParsingTask(parsing_job_id={self.parsing_job_id}, "
                f"status={self.status})>")

    def __str__(self) -> str:
        return (f"ParsingTask(parsing_job_id={self.parsing_job_id}, "
                f"status={self.status})")