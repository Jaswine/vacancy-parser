from datetime import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel


class CollectionItemSchema(BaseModel):
    id: UUID
    name: str
    created_at: Optional[datetime]
    links_count: int

    class Config:
        orm_mode = True


class CollectionFindAllSchema(BaseModel):
    page: int
    page_size: int
    total: int
    items: List[CollectionItemSchema]


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

    class Config:
        orm_mode = True


class CollectionUpdateNameData(BaseModel):
    name: str
