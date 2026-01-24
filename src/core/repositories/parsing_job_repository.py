from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import ParsingJob


class ParsingJobRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, parsing_job: ParsingJob) -> ParsingJob:
        """
        Create a new parsing job
        """
        self.session.add(parsing_job)
        await self.session.commit()
        await self.session.refresh(parsing_job)
        return parsing_job

    async def save(self, parsing_job: ParsingJob) -> None:
        """
        Save a new parsing job
        """
        await self.session.commit()
        await self.session.refresh(parsing_job)