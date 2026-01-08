from flask import Blueprint, render_template, request
from models import Restaurant # models.pyでRestaurantを定義しておく必要があります

# Blueprintの作成
list_bp = Blueprint('res_list', __name__, url_prefix='/restaurants')

@list_bp.route('/')
def list():
    # データベースからお店一覧を取得
    # 必要に応じて .order_by(Restaurant.name) などで並び替えを追加できます
    restaurants = Restaurant.select() 
    
    return render_template(
        'restaurant_list.html', 
        title='お店一覧', 
        items=restaurants # テンプレートに渡す変数
    )