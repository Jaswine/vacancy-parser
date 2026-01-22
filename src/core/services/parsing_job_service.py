import logging
from uuid import UUID

from core.db.models import ParsingJob
from core.repositories.parsing_job_repository import ParsingJobRepository

logger = logging.getLogger(__name__)

class ParsingJobService:
    def __init__(self, parsing_job_repository: ParsingJobRepository):
        self.parsing_job_repository = parsing_job_repository

    async def create_parsing_job(self, account_id: UUID, collection_id: UUID) -> ParsingJob:
        """
        Create a new parsing job
        """
        logger.info("Creating new parsing job",
                    extra={"account_id": account_id, "collection_id": collection_id})

        new_parsing_job = ParsingJob(
            account_id=account_id,
            collection_id=collection_id,
        )
        return await self.parsing_job_repository.create(new_parsing_job)
