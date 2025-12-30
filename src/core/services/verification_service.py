from datetime import datetime, timedelta

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.enums.verification_code_type import VerificationCodeType
from src.core.db.models import Account
from src.core.db.models.verification_code import VerificationCode
from src.core.repositories.account_repository import AccountRepository
from src.core.repositories.verification_repository import VerificationRepository
from src.core.utils.security import generate_code, hash_code


class VerificationService:
    CODE_TTL_MINUTES = 2

    def __init__(self, db: AsyncSession) -> None:
        self.verification_repository = VerificationRepository(db)
        self.account_repository = AccountRepository(db)

    async def create_and_send_code(self, account: Account, email_sender) -> None:
        code = generate_code()
        code_hash = hash_code(code)

        expires_at = datetime.utcnow() + timedelta(minutes=self.CODE_TTL_MINUTES)

        verification_code: VerificationCode = VerificationCode(
            account_id=account.id,
            email=account.email,
            code_hash=code_hash,
            type=VerificationCodeType.CONFIRM_ACCOUNT,
            expires_at=expires_at
        )

        await self.verification_repository.create(verification_code)

        # await email_sender.send_verification_code(
        #     to=account.email,
        #     code=code
        # )
        # publish_verification_event(
        #     account_id=account.id,
        #     email=account.email,
        #     code=code,
        # )


    async def verify_code(self, account: Account, code: str) -> bool:
        record: VerificationCode = await self.verification_repository.get_active_code_by_account_id(account.id)

        if not record or record.expires_at < datetime.utcnow():
            return False

        if record.code_hash != hash_code(code):
            record.attempts += 1
            await self.verification_repository.save(record)
            return False

        record.is_used = True
        record.used_at = datetime.utcnow()

        account.is_verified = True

        await self.verification_repository.save(record)
        await self.account_repository.save(account)
        return True

