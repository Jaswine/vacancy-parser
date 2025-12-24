from datetime import datetime

from sqlalchemy import String, DateTime, Enum
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import func

from src.core.db.enums.status import Status
from src.core.db.enums.account_type import AccountType
from src.core.db.models.base import Base


class Account(Base):
    """
    Account model
    """

    __tablename__ = "accounts"

    username: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)

    account_status: Mapped[Status] = mapped_column(
        Enum(Status), default=Status.ACTIVE, nullable=False
    )
    account_type: Mapped[AccountType] = mapped_column(
        Enum(AccountType), default=AccountType.SIMPLE, nullable=False
    )

    last_login: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=True
    )
    last_active: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=True
    )

    link_lists = relationship("LinkList", back_populates="account")
    subscriptions = relationship("Subscribe", back_populates="account")
    parsing_logs = relationship("ParsingLog", back_populates="account")

    def __repr__(self) -> str:
        return f"<Account(id={self.id}, username={self.username}, email={self.email}>"

    def __str__(self) -> str:
        return f"Account(id={self.id}, username={self.username}, email={self.email})"
