from pydantic import BaseModel
from typing import Optional, List
from entities.serviceOrder import ServiceOrderState


class ServiceOrderModel(BaseModel):
    vehicle_id: int
    current_mileage: Optional[int] = None
    maintenance_date: Optional[str] = None
    maintenance_type: Optional[str] = None
    maintenance_cost: Optional[float] = None
    service_provider: Optional[str] = None
    recommended_next_maintenance: Optional[str] = None
    notes: Optional[str] = None
    repair_history: Optional[str] = None
    vehicle_condition: Optional[str] = None
    attached_documents: Optional[str] = None
    state: Optional[ServiceOrderState] = ServiceOrderState.CREATED
    operation_description: str
    parts: Optional[List[int]] = []
    start_date: Optional[str] = None
    end_date: Optional[str] = None

    class Config:
        from_attributes = True
