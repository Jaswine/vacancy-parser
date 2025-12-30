from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import Account
from src.core.repositories.account_repository import AccountRepository
from src.core.utils.password_utils import hash_password


class AccountService:
    def __init__(self, db: AsyncSession):
        self.account_repository = AccountRepository(db)

    async def get_by_email(self, email: str) -> Account | None:
        return await self.account_repository.get_by_email(email)

    async def create_account(self, username: str, email: str, password: str) -> Account:
        """
        Creates an account with the given username and email
        """
        account: Account = Account(
            username=username,
            email=email,
            password_hash=hash_password(password),
        )
        return await self.account_repository.create(account)

    async def verify_account(self, code: str) -> Account:
        pass
