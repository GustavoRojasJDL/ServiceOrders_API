from peewee import (
    AutoField,
    Field,
    CharField,
    DateField,
    IntegerField,
    ForeignKeyField,
    DecimalField,
    TextField,
    ManyToManyField,
)
from entities.baseModel import BaseModel
from entities.vehicle import Vehicle
from entities.part import Part
from enum import Enum


class ServiceOrderState(Enum):
    CREATED = "CREATED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class ServiceOrder(BaseModel):
    id = AutoField()
    vehicle = ForeignKeyField(Vehicle, backref="service_orders")
    current_mileage = IntegerField(null=True)
    maintenance_date = DateField(null=True)
    maintenance_type = CharField(max_length=100, null=True)
    maintenance_cost = DecimalField(max_digits=10, decimal_places=2, null=True)
    service_provider = CharField(max_length=100, null=True)
    recommended_next_maintenance = DateField(null=True)
    notes = TextField(null=True)
    repair_history = TextField(null=True)
    vehicle_condition = CharField(max_length=50, null=True)
    attached_documents = TextField(null=True)
    state = CharField(max_length=20, default=ServiceOrderState.CREATED.value)
    operation_description = TextField()
    parts = ManyToManyField(Part, backref="service_orders")
    start_date = DateField(null=True, default=None)
    end_date = DateField(null=True, default=None)

    def __str__(self):
        return f"Service Order {self.id} - Vehicle {self.vehicle.brand} {self.vehicle.model}"


ServiceOrderPart = ServiceOrder.parts.get_through_model()
