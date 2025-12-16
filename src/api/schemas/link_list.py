from pydantic import BaseModel


class LinkListBase(BaseModel):
    name: str

    class Config:
        orm_mode = True
