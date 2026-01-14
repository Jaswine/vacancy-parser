from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class CollectionFindAllSchema(BaseModel):
    id: UUID
    name: str
    created_at: Optional[datetime]
    links_count: int

class CollectionFindOneSchema(BaseModel):
    id: UUID
    name: str
    created_at: Optional[datetime]
    links_count: int
