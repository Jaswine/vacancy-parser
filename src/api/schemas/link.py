from typing import List
from uuid import UUID

from pydantic import BaseModel

from src.core.schemas.link import LinkFindAllSchema


class LinkSchema(BaseModel):
    id: UUID
    url: str

    class Config:
        orm_mode = True


class LinkFindAllPaginationSchema(BaseModel):
    page: int
    page_size: int
    total: int
    items: List[LinkFindAllSchema]


class LinkDataSchema(BaseModel):
    url: str
