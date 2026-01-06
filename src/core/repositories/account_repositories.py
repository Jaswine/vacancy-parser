import uuid
from typing import Any

from sqlalchemy import func, distinct
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.enums.account_subscription_status import AccountSubscriptionStatus
from src.core.db.enums.status import Status
from src.core.db.models import Account, Collection, ParsingRun, AccountSubscription
from src.core.schemas.Account import AccountSchema


class AccountRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, account_id: uuid.UUID) -> Account | None:
        """
        Get an account by its ID
        """
        result = await self.session.execute(
            select(Account).where(Account.id == account_id)
        )
        return result.scalar_one_or_none()

    async def get_by_id_with_relations(self, account_id: uuid.UUID) -> AccountSchema | None:
        """
        Get an account by its ID
        """
        # select_account_subscriptions_subquery = (
        #     select(AccountSubscription)
        #     .where(AccountSubscription.account_id == account_id)
        #     .label("account_subscriptions")
        #     .options(
        #         selectinload(AccountSubscription.subscription),
        #     )
        # )

        stmt = (
            select(
                Account,
                func.count(distinct(Collection.id)).label("collections_count"),
                func.count(distinct(ParsingRun.id)).label("parsing_runs_count"),
            )
            .select_from(Account)
            .outerjoin(Collection, Collection.account_id == Account.id)
            .outerjoin(ParsingRun, ParsingRun.account_id == Account.id)
            .where(Account.id == account_id)
            .options(
                selectinload(Account.account_subscriptions).selectinload(AccountSubscription.subscription),
            )
            .group_by(Account.id)
        )
        result = await self.session.execute(stmt)
        row: Account | None = result.one_or_none()

        if row is None:
            return None

        account, collections_count, parsing_runs_count = row

        account.collections_count = collections_count
        account.parsing_runs_count = parsing_runs_count

        return account

    async def get_by_email(self, email: str) -> Account | None:
        """
        Get an account by its email
        """
        result = await self.session.execute(
            select(Account).where(Account.email == email)
        )
        return result.scalar_one_or_none()

    async def create(self, account: Account) -> Account:
        """
        Create a new account
        """
        self.session.add(account)
        await self.session.commit()
        await self.session.refresh(account)
        return account

    async def save(self, account: Account):
        """
        Save an account
        """
        await self.session.commit()
        await self.session.refresh(account)
