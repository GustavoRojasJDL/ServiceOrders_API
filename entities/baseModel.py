from peewee import Model, AutoField, CharField, IntegerField, DateField, DecimalField, TextField, ForeignKeyField
from database import database

class BaseModel(Model):
    class Meta:
        database = database