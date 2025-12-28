import uuid

from datetime import datetime

from sqlalchemy import ForeignKey, String, Enum, DateTime, Integer, Boolean
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship, mapped_column, Mapped

from sqlalchemy.sql import func

from src.core.db.enums.verification_code_type import VerificationCodeType
from src.core.db.models import Account
from src.core.db.models.base import Base


class VerificationCode(Base):
    """
    VerificationCode model
    """
    __tablename__ = "verification_codes"

    account_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("accounts.id"))

    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    code_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    type: Mapped[VerificationCodeType] = mapped_column(Enum(VerificationCodeType), nullable=False)
    attempts: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_used: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    account: Mapped[Account] = relationship(
        "Account", back_populates="verification_codes", foreign_keys=[account_id]
    )