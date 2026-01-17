import logging

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.dependencies.auth import get_current_user_payload
from src.api.schemas.account import AccountResponse
from src.core.db.database import get_db
from src.core.repositories.account_repository import AccountRepository
from src.core.services.account_service import AccountService

router = APIRouter(prefix="/account", tags=["Account"])

logger = logging.getLogger(__name__)


# -------------------------
# Account
# -------------------------
@router.get("/me",
            response_model=AccountResponse,
            status_code=status.HTTP_200_OK)
async def me(
    payload: dict = Depends(get_current_user_payload),
    db: AsyncSession = Depends(get_db),
):
    account_repository: AccountRepository = AccountRepository(db)
    service: AccountService = AccountService(account_repository)

    account_id = payload["sub"]

    try:
        account = await service.get_by_id_with_relations(account_id)

        if not account:
            logger.warning(
                "Account not found",
                extra={"id": account_id},
            )
            raise HTTPException(status_code=401, detail="Invalid id")

        return AccountResponse(
            username=account.username,
            email=account.email,
            last_login=account.last_login,
            created_at=account.created_at,
            collections_count=account.collections_count,
            # subscriptions=account.subscriptions,
            parsing_runs_count=account.parsing_runs_count,
        )
    except Exception:
        logger.exception(
            "Unexpected error during finding account",
            extra={"id": account_id},
        )
        raise
