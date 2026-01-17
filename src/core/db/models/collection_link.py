import uuid

from sqlalchemy import ForeignKey, Enum
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship, mapped_column, Mapped

from src.core.db.enums.status import Status
from src.core.db.models.base import Base


class CollectionLink(Base):
    """
    CollectionLink model
    """

    __tablename__ = "collection_links"

    collection_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("collections.id"), primary_key=True
    )
    link_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("links.id"), primary_key=True
    )

    collection = relationship(
        "Collection", back_populates="collection_links", foreign_keys=[collection_id]
    )
    link = relationship(
        "Link", back_populates="collection_links", foreign_keys=[link_id]
    )

    activity_status: Mapped[Status] = mapped_column(
        Enum(Status), default=Status.ACTIVE, nullable=False
    )

    def __repr__(self) -> str:
        return (
            f"<CollectionLink(collection_id={self.collection_id}, "
            f"link_id={self.link_id}),"
            f"activity_status={self.activity_status})>"
        )

    def __str__(self) -> str:
        return (
            f"CollectionLink(collection_id={self.collection_id}, "
            f"link_id={self.link_id},"
            f"activity_status={self.activity_status})"
        )
