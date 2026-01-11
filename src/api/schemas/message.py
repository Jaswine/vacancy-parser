from pydantic import BaseModel


class MessageSuccess(BaseModel):
    message: str


class ErrorMessage(BaseModel):
    statusCode: int
    message: str
