from pydantic import BaseModel
from typing import Optional


class PartModel(BaseModel):
    name: str
    description: Optional[str] = None

    class Config:
        from_attributes: True
