from sqlalchemy import Integer, ForeignKey, String, Enum
from sqlalchemy.orm import relationship, mapped_column, Mapped

from src.core.db.enums.status import Status
from src.core.db.models.base import Base


class Link(Base):
    """
    Link model
    """

    __tablename__ = "links"

    company_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    url: Mapped[str] = mapped_column(String(1500), nullable=False, index=True)
    activity_status: Mapped[Status] = mapped_column(
        Enum(Status), default=Status.ACTIVE, nullable=False
    )

    link_list_id: Mapped[int] = mapped_column(Integer, ForeignKey("link_lists.id"))
    link_list = relationship(
        "LinkList", back_populates="links", foreign_keys=[link_list_id]
    )

    def __repr__(self) -> str:
        return (
            f"<Link(id={self.id}, link_list_id={self.link_list_id}, "
            f"company_name={self.company_name}, url={self.url})>"
        )

    def __str__(self) -> str:
        return (
            f"Link(id={self.id}, link_list_id={self.link_list_id}, "
            f"company_name={self.company_name}, url={self.url})>"
        )
