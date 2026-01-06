from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

from src.api.schemas.subscription import SubscriptionSchema


class AccountSchema(BaseModel):
    username: str
    email: str
    last_login: Optional[datetime]
    created_at: Optional[datetime]
    collections_count: int
    parsing_runs_count: int
    subscriptions: List[SubscriptionSchema] = []
