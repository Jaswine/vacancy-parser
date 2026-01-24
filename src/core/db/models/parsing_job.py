import uuid


from datetime import datetime

from sqlalchemy import Integer, ForeignKey, DateTime, Enum
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import func

from src.core.db.enums.job_status import JobStatus
from src.core.db.models.base import Base


class ParsingJob(Base):
    """
    ParsingJob model
    """

    __tablename__ = "parsing_jobs"

    account_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("accounts.id")
    )
    collection_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("collections.id")
    )

    status: Mapped[JobStatus] = mapped_column(
        Enum(JobStatus), default=JobStatus.CREATED, nullable=False
    )

    started_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    finished_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    duration: Mapped[int] = mapped_column(Integer, default=0, nullable=True)

    links_total: Mapped[int | None] = mapped_column(Integer, default=0, nullable=True)
    links_processed: Mapped[int | None] = mapped_column(
        Integer, default=0, nullable=True
    )

    vacancies_found: Mapped[int | None] = mapped_column(
        Integer, default=0, nullable=True
    )
    errors_count: Mapped[int | None] = mapped_column(Integer, default=0, nullable=True)


    account = relationship(
        "Account", back_populates="parsing_jobs", foreign_keys=[account_id]
    )
    collection = relationship(
        "Collection", back_populates="parsing_jobs", foreign_keys=[collection_id]
    )

    parsing_tasks = relationship("ParsingTask",
                                 back_populates="parsing_job")


    def __repr__(self) -> str:
        return (
            f"<ParsingJob(id={self.id}, account_id={self.account_id}, "
            f"collection_id={self.collection_id}, start_time={self.started_at}, "
            f"end_time={self.finished_at}, vacancies_found={self.vacancies_found}, "
            f"errors_count={self.errors_count})>"
        )

    def __str__(self) -> str:
        return (
            f"ParsingJob(id={self.id}, account_id={self.account_id}, "
            f"collection_id={self.collection_id}, start_time={self.started_at}, "
            f"end_time={self.finished_at}, vacancies_found={self.vacancies_found}, "
            f"errors_count={self.errors_count}"
        )
