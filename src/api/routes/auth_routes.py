import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.account import (
    AccountRegistrationData,
    TokenResponse,
    AccountLoginData,
)
from src.api.utils.jwt_utils import create_access_token
from src.core.repositories.verification_repository import VerificationRepository
from src.core.services.verification_service import VerificationService
from src.core.utils.password_utils import verify_password
from src.core.db.database import get_db
from src.core.db.models import Account
from src.core.repositories.account_repository import AccountRepository
from src.core.services.account_service import AccountService

router = APIRouter(prefix="/auth", tags=["Auth"])

logger = logging.getLogger(__name__)


# -------------------------
# Registration
# -------------------------
@router.post("/registration")
async def registration(
    user: AccountRegistrationData, db: AsyncSession = Depends(get_db)
):
    logger.info("Registration attempt", extra={"email": user.email})

    service: AccountService = AccountService(db)
    verification_service: VerificationService = VerificationService(db)

    try:
        existing = await service.get_by_email(user.email)

        # If email already exists
        if existing:
            logger.warning(
                "Registration failed: email already exists",
                extra={"email": user.email},
            )
            raise HTTPException(status_code=400, detail="Email already registered")

        # Create a new account
        new_account: Account = await service.create_account(
            user.username, user.email, user.password
        )

        # Verification code creating and sending
        verification = await verification_service.create_and_send_code(new_account)

        logger.info(
            "Account successfully registered",
            extra={"account_id": str(new_account.id), "email": user.email},
        )

        token = create_access_token({"sub": str(new_account.id)})
        return TokenResponse(access_token=token)
    except Exception:
        logger.exception(
            "Unexpected error during registration",
            extra={"email": user.email},
        )
        raise


# -------------------------
# Sign In
# -------------------------
@router.post("/sign-in", response_model=TokenResponse)
async def sign_in(
    user: AccountLoginData,
    db: AsyncSession = Depends(get_db),
):
    logger.info("Login attempt", extra={"email": user.email})

    account_repository: AccountRepository = AccountRepository(db)
    service: AccountService = AccountService(account_repository)

    try:
        account = await service.get_by_email(user.email)

        if not account:
            logger.warning(
                "Login failed: account not found",
                extra={"email": user.email},
            )
            raise HTTPException(status_code=401, detail="Invalid email or password")

        if not verify_password(user.password, account.password_hash):
            logger.warning(
                "Login failed: invalid password",
                extra={"account_id": str(account.id)},
            )
            raise HTTPException(status_code=401, detail="Invalid email or password")

        token = create_access_token({"sub": str(account.id)})

        logger.info(
            "Login successful",
            extra={
                "account_id": str(account.id),
                "email": user.email,
            },
        )

        return TokenResponse(access_token=token)
    except Exception:
        logger.exception(
            "Unexpected error during sign-in",
            extra={"email": user.email},
        )
        raise
