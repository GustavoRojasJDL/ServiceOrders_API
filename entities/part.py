from peewee import AutoField, CharField, TextField
from entities.baseModel import BaseModel

class Part(BaseModel):
    id = AutoField()
    name = CharField(max_length=100)
    description = TextField(null=True)