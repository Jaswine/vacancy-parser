import uuid

from datetime import datetime

from sqlalchemy import ForeignKey, String, Enum, Numeric, DateTime
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship, mapped_column, Mapped

from src.core.db.enums.invoice_status import InvoiceStatus
from src.core.db.models.base import Base


class Invoice(Base):
    """
    Invoice model
    """

    __tablename__ = "invoices"

    account_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("accounts.id")
    )
    subscription_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("subscriptions.id")
    )

    amount: Mapped[int | None] = mapped_column(Numeric(10, 2), default=0, nullable=True)
    currency: Mapped[str | None] = mapped_column(
        String(3), nullable=True, default="USDT"
    )

    status: Mapped[InvoiceStatus] = mapped_column(
        Enum(InvoiceStatus), default=InvoiceStatus.DRAFT, nullable=False
    )

    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    paid_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

    payment_url = mapped_column(String(1000), nullable=True)

    account = relationship(
        "Account", back_populates="invoices", foreign_keys=[account_id]
    )
    subscription = relationship(
        "Subscription", back_populates="invoices", foreign_keys=[subscription_id]
    )

    transactions = relationship("Transaction", back_populates="invoice")

    def __repr__(self) -> str:
        return (
            f"<Invoice(id={self.id}, account_id={self.account_id}, "
            f"amount={self.amount}{self.currency}, status={self.status})>"
        )

    def __str__(self) -> str:
        return (
            f"Invoice(id={self.id}, account_id={self.account_id}, "
            f"amount={self.amount}{self.currency}, status={self.status})>)"
        )
