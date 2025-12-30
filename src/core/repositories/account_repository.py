from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import Account


class AccountRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_email(self, email: str) -> Account | None:
        """
        Gets account by email
        """
        result = await self.session.execute(
            select(Account).where(Account.email == email)
        )
        return result.scalar_one_or_none()

    async def create(self, account: Account) -> Account:
        """
        Creates a new account
        """
        self.session.add(account)
        await self.session.commit()
        await self.session.refresh(account)
        return account

    async def save(self, account: Account):
        """
        Save account
        """
        await self.session.commit()
        await self.session.refresh(account)
