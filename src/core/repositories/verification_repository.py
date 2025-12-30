import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.core.db.models.verification_code import VerificationCode


class VerificationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, verification_code: VerificationCode) -> VerificationCode:
        """
        Saves a verification code
        """
        self.session.add(verification_code)
        await self.session.commit()
        await self.session.refresh(verification_code)
        return verification_code

    async def get_active_code_by_account_id(self, account_id: uuid.UUID) ->  VerificationCode | None:
        """
        Gets a verification code by its account id
        """
        result = await self.session.execute(
            select(VerificationCode).where(VerificationCode.account_id == account_id)
        )
        return result.scalar_one_or_none()

    async def save(self, verification_code: VerificationCode):
        """
        Save verification code
        """
        await self.session.commit()
        await self.session.refresh(verification_code)
