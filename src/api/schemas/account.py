from datetime import date, datetime
from typing import Optional, List
from pydantic import BaseModel

from src.api.schemas.account_subscription import AccountSubscriptionSchema


class AccountEmail(BaseModel):
    email: str


class AccountLoginData(AccountEmail):
    password: str


class AccountRegistrationData(AccountLoginData):
    username: str


class AccountResponse(AccountEmail):
    username: str
    email: str

    last_login: Optional[datetime]
    created_at: Optional[datetime]

    collections_count: int
    parsing_runs_count: int

    subscriptions: List[AccountSubscriptionSchema] = []

    class Config:
        # orm_mode = True
        from_attributes = True
