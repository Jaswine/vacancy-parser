from datetime import date
from typing import Optional, List

from pydantic import BaseModel

from schemas.link_list import LinkListBase


class AccountEmail(BaseModel):
    email: str

class AccountLoginData(AccountEmail):
    password: str

class AccountRegistrationData(AccountLoginData):
    username: str

class AccountResponse(AccountEmail):
    username: str

    last_login: Optional[date]
    last_active: Optional[date]

    link_lists: List[LinkListBase] = []

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
