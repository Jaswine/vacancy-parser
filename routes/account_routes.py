from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from configs.database_config import get_db
from schemas.account import AccountRegistrationData, Token, AccountLoginData
from models.account import Account
from utils.security import hash_password, create_access_token, verify_password

router = APIRouter()

# Registration
@router.post("/registration/")
async def registration(user: AccountRegistrationData, db: AsyncSession = Depends(get_db)):
    # Check if email exists
    result = await db.execute(select(Account).filter(Account.email == user.email))
    existing = result.scalars().first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create account
    new_account = Account(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
    )
    db.add(new_account)
    await db.commit()
    await db.refresh(new_account)

    # Return JWT
    token = create_access_token({"sub": str(new_account.id)})
    return Token(access_token=token)

# Login
@router.post("/login/", response_model=Token)
async def login(user: AccountLoginData, db: AsyncSession = Depends(get_db)):
    print("USER EMAIL: " + user.email)
    result = await db.execute(select(Account).filter(Account.email == user.email))
    account = result.scalars().first()

    if not account or not verify_password(user.password, account.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"sub": str(account.id)})
    return Token(access_token=token)