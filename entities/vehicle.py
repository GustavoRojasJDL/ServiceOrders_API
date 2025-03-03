from peewee import AutoField, CharField, TextField, IntegerField
from entities.baseModel import BaseModel


class Vehicle(BaseModel):
    id = AutoField()
    brand = CharField(max_length=50)
    model = CharField(max_length=50)
    year = IntegerField()
    plate = CharField(max_length=20)
    vin = CharField(max_length=50, null=True, default=None)
    purchase_date = TextField(null=True, default=None)
    warranty = CharField(max_length=100, null=True, default=None)
    fuel_type = CharField(max_length=50, null=True, default=None)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - Plate: {self.plate}"
