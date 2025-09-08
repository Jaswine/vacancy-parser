from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from configs.database_config import get_db
from schemas.account import AccountResponse
from models.account import Account

router = APIRouter()

@router.get("/", response_model=list[AccountResponse])
async def show_all_accounts(db: AsyncSession = Depends(get_db)):
    print("Show all accounts!")
    result = await db.execute(select(Account))
    accounts = result.scalars().all()
    return accounts