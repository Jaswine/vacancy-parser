from sqlalchemy import Integer, ForeignKey, String, Enum
from sqlalchemy.orm import relationship, mapped_column, Mapped

from src.core.db.enums.status import Status
from src.core.db.models import Account
from src.core.db.models.base import Base


class LinkList(Base):
    """
    LinkList model
    """

    __tablename__ = "link_lists"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    activity_status: Mapped[Status] = mapped_column(
        Enum(Status), default=Status.ACTIVE, nullable=False
    )

    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("accounts.id"))
    account: Mapped[Account] = relationship(
        "Account", back_populates="link_lists", foreign_keys=[account_id]
    )

    links = relationship("Link", back_populates="link_list")
    parsing_logs = relationship("ParsingLog", back_populates="link_list")
    filters = relationship("Filter", back_populates="link_list")

    def __repr__(self) -> str:
        return f"<LinkList(id={self.id}, name={self.name}, activity_status={self.activity_status})>"

    def __str__(self) -> str:
        return f"LinkList(id={self.id}, name={self.name}, activity_status={self.activity_status})"
