from datetime import datetime
from typing import Optional, List

from aiokafka.protocol.types import Schema

from src.api.schemas.subscription import SubscriptionSchema


class AccountSchema(Schema):
    username: str
    email: str
    last_login: Optional[datetime]
    created_at: Optional[datetime]
    collections_count: int
    parsing_runs_count: int
    subscriptions: List[SubscriptionSchema] = []
