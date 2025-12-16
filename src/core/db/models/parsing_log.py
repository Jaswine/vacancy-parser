from datetime import datetime

from sqlalchemy import Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import func

from src.core.db.models.base import Base


class ParsingLog(Base):
    """
    Parsing Logs model
    """

    __tablename__ = "parsing_logs"

    start_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    end_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    jobs_found: Mapped[int | None] = mapped_column(Integer, default=0, nullable=True)
    errors: Mapped[int | None] = mapped_column(Integer, default=0, nullable=True)

    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("accounts.id"))
    account = relationship(
        "Account", back_populates="parsing_logs", foreign_keys=[account_id]
    )

    link_list_id: Mapped[int] = mapped_column(Integer, ForeignKey("link_lists.id"))
    link_list = relationship(
        "LinkList", back_populates="parsing_logs", foreign_keys=[link_list_id]
    )

    def __repr__(self) -> str:
        return (
            f"<ParsingLog(id={self.id}, account_id={self.account_id}, "
            f"link_list_id={self.link_list_id}, start_time={self.start_time}, "
            f"end_time={self.end_time}, jobs_found={self.jobs_found}, errors={self.errors})>"
        )

    def __str__(self) -> str:
        return (
            f"ParsingLog(id={self.id}, account_id={self.account_id}, "
            f"link_list_id={self.link_list_id}, start_time={self.start_time}, "
            f"end_time={self.end_time}, jobs_found={self.jobs_found}, errors={self.errors})>"
        )
