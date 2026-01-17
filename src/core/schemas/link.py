from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class LinkFindAllSchema(BaseModel):
    id: UUID
    url: str
