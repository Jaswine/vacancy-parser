from sqlalchemy import ForeignKey, String, Numeric
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship, mapped_column, Mapped

from src.core.db.enums.transaction_provider import TransactionProvider
from src.core.db.enums.transaction_status import TransactionStatus
from src.core.db.models.base import Base


class Transaction(Base):
    """
    Transaction model
    """

    __tablename__ = "transactions"

    account_id: Mapped[int] = mapped_column(
        UUID(as_uuid=True), ForeignKey("accounts.id")
    )
    invoice_id: Mapped[int] = mapped_column(
        UUID(as_uuid=True), ForeignKey("invoices.id")
    )

    amount: Mapped[int | None] = mapped_column(Numeric(10, 2), default=0, nullable=True)
    currency: Mapped[str | None] = mapped_column(
        String(3), nullable=True, default="USDT"
    )

    status: Mapped[TransactionStatus] = mapped_column(
        String(255), nullable=True, default=TransactionStatus.PENDING
    )
    provider: Mapped[TransactionProvider] = mapped_column(
        String(255), nullable=True, default=TransactionProvider.STRIPE
    )

    provider_tx_id: Mapped[str] = mapped_column(String(255), nullable=True, default="")

    account = relationship(
        "Account", back_populates="transactions", foreign_keys=[account_id]
    )
    invoice = relationship(
        "Invoice", back_populates="transactions", foreign_keys=[invoice_id]
    )

    def __repr__(self) -> str:
        return (
            f"<Transaction(id={self.id}, account_id={self.account_id}, invoice_id={self.invoice_id}"
            f"amount={self.amount}{self.currency}, status={self.status}, provider={self.provider})>"
        )

    def __str__(self) -> str:
        return (
            f"Transaction(id={self.id}, account_id={self.account_id}, invoice_id={self.invoice_id}"
            f"amount={self.amount}{self.currency}, status={self.status}, provider={self.provider})"
        )
