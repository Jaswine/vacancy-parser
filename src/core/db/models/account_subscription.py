import uuid

from datetime import datetime

from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.dialects.postgresql import UUID

from src.core.db.enums.account_subscription_status import AccountSubscriptionStatus
from src.core.db.models.base import Base


class AccountSubscription(Base):
    """
    AccountSubscription model
    """

    __tablename__ = "account_subscriptions"

    account_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("accounts.id")
    )
    subscription_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("subscriptions.id")
    )

    starts_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

    status: Mapped[AccountSubscriptionStatus] = mapped_column(
        String(255), nullable=True
    )

    account = relationship(
        "Account", back_populates="account_subscriptions", foreign_keys=[account_id]
    )
    subscription = relationship(
        "Subscription",
        back_populates="account_subscriptions",
        foreign_keys=[subscription_id],
    )

    def __repr__(self) -> str:
        return (
            f"<AccountSubscription(id={self.id}, account_id={self.account_id}, subscription_id={self.subscription_id}"
            f"starts_at={self.starts_at}, expires_at={self.expires_at}, status={self.status})>"
        )

    def __str__(self) -> str:
        return (
            f"AccountSubscription(id={self.id}, account_id={self.account_id}, subscription_id={self.subscription_id}"
            f"starts_at={self.starts_at}, expires_at={self.expires_at}, status={self.status})"
        )
