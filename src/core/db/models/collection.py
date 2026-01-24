import uuid

from sqlalchemy import ForeignKey, String, Enum
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship, mapped_column, Mapped

from src.core.db.enums.status import Status
from src.core.db.models import Account
from src.core.db.models.base import Base


class Collection(Base):
    """
    Collection model
    """

    __tablename__ = "collections"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    activity_status: Mapped[Status] = mapped_column(
        Enum(Status), default=Status.ACTIVE, nullable=False
    )

    account_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("accounts.id")
    )
    account: Mapped[Account] = relationship(
        "Account", back_populates="collections", foreign_keys=[account_id]
    )

    collection_links = relationship(
        "CollectionLink", back_populates="collection", cascade="all, delete-orphan"
    )

    links = relationship(
        "Link", secondary="collection_links", back_populates="collections"
    )

    parsing_jobs = relationship("ParsingJob", back_populates="collection")
    filters = relationship("Filter", back_populates="collection")

    def __repr__(self) -> str:
        return f"<Collection(id={self.id}, name={self.name}, activity_status={self.activity_status})>"

    def __str__(self) -> str:
        return f"Collection(id={self.id}, name={self.name}, activity_status={self.activity_status})"
