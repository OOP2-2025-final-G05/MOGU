

MODELS = [
    Restaurant, # 飲食店情報テーブル
    Review      # レビュー情報テーブル
]

# app.py などで呼び出す初期化処理
def initialize_database():
    db.connect()
    # MODELSリストに含まれるテーブルを自動作成
    db.create_tables(MODELS, safe=True)