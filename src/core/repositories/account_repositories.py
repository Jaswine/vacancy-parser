from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import Account


class AccountRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_email(self, email: str) -> Account | None:
        result = await self.session.execute(
            select(Account).where(Account.email == email)
        )
        return result.scalars().first()

    async def create(self, account: Account) -> Account:
        self.session.add(account)
        await self.session.commit()
        await self.session.refresh(account)
        return account