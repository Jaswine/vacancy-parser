import logging
import uuid

from datetime import datetime

from src.core.db.models import Account
from src.core.repositories.account_repositories import AccountRepository
from src.core.schemas.Account import AccountSchema
from src.core.utils.password_utils import hash_password

logger = logging.getLogger(__name__)


class AccountService:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    async def get_by_id_with_relations(self, account_id: uuid.UUID) -> AccountSchema | None:
        """
        Get an account by its ID
        """
        result = await self.account_repository.get_by_id_with_relations(account_id)
        return result

    async def get_by_email(self, email: str) -> Account | None:
        """
        Gets an account with the given email
        """
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

    async def update_last_login_time(self, account: Account) -> None:
        """
        Updates the last login time of the given account
        """
        account.last_login = datetime.utcnow()
        await self.account_repository.save(account)
