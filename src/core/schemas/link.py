from uuid import UUID

from pydantic import BaseModel


class LinkFindAllSchema(BaseModel):
    id: UUID
    url: str
