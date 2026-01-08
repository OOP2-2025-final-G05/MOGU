from peewee import Model, ForeignKeyField, DateTimeField, CharField
from decimal import Decimal
from .db import db

class Detail(Model):
    address = CharField(default="不明")
    genre = CharField(default="未分類")
    # order_date = DateTimeField()

    class Meta:
        database = db