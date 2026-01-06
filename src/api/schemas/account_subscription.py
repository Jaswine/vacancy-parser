from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from src.api.schemas.subscription import SubscriptionSchema


class AccountSubscriptionSchema(BaseModel):
    starts_at: Optional[datetime]
    expires_at: Optional[datetime]
    status: str

    subscription: SubscriptionSchema

    class Config:
        from_attributes = True