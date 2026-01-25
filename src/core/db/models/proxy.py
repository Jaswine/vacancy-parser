from datetime import datetime

from sqlalchemy import String, DateTime, Enum, Text, Integer
from sqlalchemy.orm import mapped_column, Mapped

from src.core.db.enums.proxy_status import ProxyStatus
from src.core.db.models.base import Base

class Proxy(Base):
    """
    Proxy model
    """

    __tablename__ = "proxies"

    url: Mapped[str] = mapped_column(String(1500), nullable=False, unique=True)
    status: Mapped[ProxyStatus] = mapped_column(Enum(ProxyStatus),
                                                default=ProxyStatus.ACTIVE, nullable=False)

    success_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    fail_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    last_checked_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now())

    def __repr__(self) -> str:
        return f"<Proxy(url={self.url}, status={self.status})>"

    def __str__(self) -> str:
        return f"Proxy(url={self.url}, status={self.status})"