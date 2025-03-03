from pydantic import BaseModel
from typing import Optional


class VehicleModel(BaseModel):
    brand: str
    model: str
    year: int
    plate: str
    vin: Optional[str] = None
    purchase_date: Optional[str] = None
    warranty: Optional[str] = None
    fuel_type: Optional[str] = None

    class Config:
        from_attributes = True
