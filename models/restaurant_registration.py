from peewee import Model, CharField
from .db import db

class Restaurant(Model):
    name = CharField()
    address = CharField()
    genre = CharField()
    price = CharField()
    time = CharField()

    class Meta:
        database = db