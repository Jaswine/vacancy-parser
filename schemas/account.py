from pydantic import BaseModel
from datetime import date
from typing import Optional, List

class AccountBase(BaseModel):
    email: str

class AccountSignInRequest(AccountBase):
    password: str

class AccountSignUpRequest(AccountSignInRequest):
    username: str

class AccountInfo(AccountBase):
    username: str

class AccountType(BaseModel):
    account_type: str
