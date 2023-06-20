from typing import Optional, List
from pydantic import BaseModel


class VowelCountRequest(BaseModel):
    words: List[Optional[str]]


class SortRequest(BaseModel):
    words: List[Optional[str]]
    order: str
