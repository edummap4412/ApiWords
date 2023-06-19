from typing import Optional
from pydantic import BaseModel


class WordSchema(BaseModel):
    word: Optional[str] = None

    class Config:
        orm_mode = True
