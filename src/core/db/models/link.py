from sqlalchemy import String, Enum
from sqlalchemy.orm import relationship, mapped_column, Mapped

from src.core.db.enums.status import Status
from src.core.db.models.base import Base


class Link(Base):
    """
    Link model
    """

    __tablename__ = "links"

    url: Mapped[str] = mapped_column(String(1500), nullable=False, index=True)
    status: Mapped[Status] = mapped_column(
        Enum(Status), default=Status.ACTIVE, nullable=False
    )

    collection_links = relationship(
        "CollectionLink", back_populates="link", cascade="all, delete-orphan"
    )

    collections = relationship(
        "Collection", secondary="collection_links", back_populates="links"
    )

    parsing_tasks = relationship("ParsingTask", back_populates="link")

    def __repr__(self) -> str:
        return f"<Link(url={self.url})>"

    def __str__(self) -> str:
        return f"Link(url={self.url})>"
