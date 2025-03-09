from pydantic import BaseModel

class AccountBase(BaseModel):
    """
        Base account schema
    """
    email: str

class AccountSignInRequest(AccountBase):
    """
        Account sign in schema
    """
    password: str

class AccountSignUpRequest(AccountSignInRequest):
    """
        Account sign up schema
    """
    username: str

class AccountInfo(AccountBase):
    """
        Account information schema
    """
    username: str

class AccountType(BaseModel):
    """
        Account tyoe schema
    """
    account_type: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
