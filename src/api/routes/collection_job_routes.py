import logging
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends, HTTPException, Query, status, Response
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas.job import JobURLsDataSchema, JobCreationResponseSchema
from src.core.db.enums.job_status import JobStatus
from src.core.db.enums.status import Status
from src.core.db.models import ParsingJob
from src.core.repositories.collection_repository import CollectionRepository
from src.core.repositories.parsing_job_repository import ParsingJobRepository
from src.core.services.collection_service import CollectionService
from src.core.services.parsing_job_service import ParsingJobService
from src.api.dependencies.auth import get_current_user_payload
from src.core.db.database import get_db

router = APIRouter(prefix="/collections", tags=["ParsingJob"])

logger = logging.getLogger(__name__)


# -------------------------
# Create a new job
# -------------------------
@router.post("/{collection_id}/jobs",
            response_model=JobCreationResponseSchema,
            status_code=status.HTTP_201_CREATED)
async def create_job(
    collection_id: UUID,
    data: JobURLsDataSchema,
    payload: dict = Depends(get_current_user_payload),
    db: AsyncSession = Depends(get_db),
):
    """
    Create a new job
    """
    collection_repository: CollectionRepository = CollectionRepository(db)
    collection_service: CollectionService = CollectionService(collection_repository)

    parsing_job_repository: ParsingJobRepository = ParsingJobRepository(db)
    parsing_job_service: ParsingJobService = ParsingJobService(parsing_job_repository)

    account_id = payload["sub"]

    try:
        # Get collection by id
        collection = await collection_service.find_collection_by_id(collection_id)
        if not collection:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Collection not found",
            )

        # Create a Parsing Job
        parsing_job: ParsingJob = await parsing_job_service.create_parsing_job(account_id, collection_id)

        # Create a Kafka consumer / producer (get data from links)

        return JobCreationResponseSchema(
            job_id=parsing_job.id,
            status=parsing_job.status,
        )
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(err)
        )