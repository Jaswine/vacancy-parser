from datetime import datetime
from typing import Optional, List
from uuid import UUID

from src.core.schemas.collection import CollectionFindAllSchema

from pydantic import BaseModel


class CollectionItemSchema(BaseModel):
    id: UUID
    name: str
    created_at: Optional[datetime]
    links_count: int

    model_config = {
        "from_attributes": True
    }

class CollectionFindAllPaginationSchema(BaseModel):
    page: int
    page_size: int
    total: int
    items: List[CollectionFindAllSchema]


class CollectionCreateData(BaseModel):
    name: str


class CollectionCreateSchema(BaseModel):
    id: UUID
    name: str
    created_at: Optional[datetime]


class CollectionFindOneSchema(BaseModel):
    id: UUID
    name: str
    created_at: Optional[datetime]
    links_count: int

    model_config = {
        "from_attributes": True
    }


class CollectionUpdateNameData(BaseModel):
    name: str
