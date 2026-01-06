import uuid
from typing import List

from pydantic import BaseModel


class SubscriptionSchema(BaseModel):
    id: uuid.UUID
    name: str
    links_per_hour: int = 0
    price: float = 0.0
    currency: str = "USD"
    description: str = ""
    features: List[str] = []

    class Config:
        from_attributes = True