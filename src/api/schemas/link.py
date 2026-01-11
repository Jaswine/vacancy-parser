from uuid import UUID

from pydantic import BaseModel


class LinkSchema(BaseModel):
    id: UUID
    url: str

    class Config:
        orm_mode = True
