from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship, mapped_column, Mapped

from src.core.db.models.base import Base


class CollectionLink(Base):
    """
    CollectionLink model
    """

    __tablename__ = "collection_links"

    collection_id: Mapped[int] = mapped_column(
        UUID(as_uuid=True), ForeignKey("collections.id"), primary_key=True
    )
    link_id: Mapped[int] = mapped_column(
        UUID(as_uuid=True), ForeignKey("links.id"), primary_key=True
    )

    collection = relationship(
        "Collection", back_populates="collection_links", foreign_keys=[collection_id]
    )
    link = relationship(
        "Link", back_populates="collection_links", foreign_keys=[link_id]
    )

    def __repr__(self) -> str:
        return (
            f"<CollectionLink(collection_id={self.collection_id}, "
            f"link_id={self.link_id})>"
        )

    def __str__(self) -> str:
        return (
            f"CollectionLink(collection_id={self.collection_id}, "
            f"link_id={self.link_id})"
        )
