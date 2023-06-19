from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar("T")


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


class WordSchema(BaseModel):
    word: Optional[str] = None

    class Config:
        orm_mode = True


class RequestWord(BaseModel):
    parameter: WordSchema = Field(...)
