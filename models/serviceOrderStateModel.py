from pydantic import BaseModel
from typing import Optional, List
from entities.serviceOrder import ServiceOrderState


class ServiceOrderStateModel(BaseModel):
    state: ServiceOrderState
