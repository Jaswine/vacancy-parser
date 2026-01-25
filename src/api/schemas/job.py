from typing import List
from uuid import UUID

from pydantic import BaseModel

from core.db.enums.job_status import JobStatus


class JobURLsDataSchema(BaseModel):
    urls: List[str]

class JobCreationResponseSchema(BaseModel):
    job_id: UUID
    status: JobStatus