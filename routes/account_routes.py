from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from configs.database_config import get_db
from schemas.account import TokenResponse, AccountSignInRequest, AccountSignUpRequest
from services.account_services import find_account_by_email_or_username, change_account_last_login_date_time, create_account
from utils.password_utils import verify_password, create_tokens

router = APIRouter()

@router.post('/sign-in', status_code=200, response_model=TokenResponse,
             name='Sign in to account')
async def sign_in_endpoint(account_data: AccountSignInRequest, db: AsyncSession = Depends(get_db)) -> TokenResponse | HTTPException:
    """
        Sign in to account endpoint
    """
    # Find an account by email
    account = await find_account_by_email_or_username(db, account_data.email)
    if not account or not verify_password(account.password, account_data.password):
        raise HTTPException(status_code=401, detail='Account not found')

    # Change account last login date time
    await change_account_last_login_date_time(db, account)
    # Access and Refresh tokens generation
    tokens = create_tokens({'sub': account.username})
    return TokenResponse(**tokens)


@router.post('/sign-up', status_code=200, response_model=TokenResponse,
             name='Sign up to account')
async def sign_up_endpoint(account_data: AccountSignUpRequest, db: AsyncSession = Depends(get_db)) -> TokenResponse | HTTPException:
    """
        Sign up to account endpoint
    """
    # Find an account by email
    if await find_account_by_email_or_username(db, account_data.email) is not None:
        raise HTTPException(status_code=401, detail='Account with this email has been already created!')

    print("Creating account")
    # Create a new account
    new_account = await create_account(db, account_data.username,
                                       account_data.email, account_data.password)
    if new_account is None:
        raise HTTPException(status_code=401, detail='Account creation has been failed!')

    # Access and Refresh tokens generation
    tokens = create_tokens({'sub': new_account.username})
    return TokenResponse(**tokens)


