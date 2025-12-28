
from src.core.db.models import Account
from src.core.repositories.account_repositories import AccountRepository
from src.core.utils.password_utils import hash_password


class AccountService:

    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    async def get_by_email(self, email: str) -> Account:
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
