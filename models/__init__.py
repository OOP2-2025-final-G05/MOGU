from peewee import Model, CharField, IntegerField, TextField, DateTimeField, ForeignKeyField
from .db import db # db.py から接続定義を読み込み
import datetime

class Restaurant(Model):
    name = CharField()          # お店名
    address = CharField()       # お店住所
    genre = CharField()         # ジャンル
    min_price = IntegerField()  # 価格帯(下限)
    max_price = IntegerField()  # 価格帯(上限)
    opening_hours = CharField() # 営業時間

    class Meta:
        database = db

class Review(Model):
    # どのお店へのレビューか (Restaurantモデルと紐付け)
    restaurant = ForeignKeyField(Restaurant, backref='reviews', on_delete='CASCADE')
    rating = IntegerField()     # 評価 (1〜5)
    comment = TextField()       # コメント
    age = IntegerField()        # 投稿者の年齢
    gender = CharField()        # 投稿者の性別
    created_at = DateTimeField(default=datetime.datetime.now) # 投稿日時

    class Meta:
        database = db

MODELS = [
    Restaurant,
    Review,
]

def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()