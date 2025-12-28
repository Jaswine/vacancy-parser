from sqlalchemy import Integer, String, Enum, Numeric, JSON
from sqlalchemy.orm import relationship, mapped_column, Mapped

from src.core.db.enums.status import Status
from src.core.db.models.base import Base


class Subscription(Base):
    """
    Subscription model
    """

    __tablename__ = "subscriptions"

    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    status: Mapped[Status] = mapped_column(
        Enum(Status), default=Status.ACTIVE, nullable=False
    )
    links_per_hour: Mapped[int | None] = mapped_column(
        Integer, default=0, nullable=True
    )
    price: Mapped[int | None] = mapped_column(Numeric(10, 2), default=0, nullable=True)
    currency: Mapped[str | None] = mapped_column(
        String(3), nullable=True, default="USDT"
    )
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)
    extra_futures: Mapped[int | None] = mapped_column(JSON, nullable=False, default=[])

    invoices = relationship("Invoice", back_populates="subscription")
    account_subscriptions = relationship("AccountSubscription", back_populates="subscription")

    def __repr__(self) -> str:
        return (
            f"<Subscription(name={self.name}, status={self.status}, "
            f"links_per_hour={self.links_per_hour}, price={self.price}{self.currency})>"
        )

    def __str__(self) -> str:
        return (
            f"Subscription(name={self.name}, status={self.status}, "
            f"links_per_hour={self.links_per_hour}, price={self.price}{self.currency})"
        )
