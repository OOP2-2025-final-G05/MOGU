from flask import Blueprint, render_template, abort
from models import Restaurant

# Blueprintの作成
details_bp = Blueprint('res_details', __name__, url_prefix='/restaurants')

@details_bp.route('/<int:restaurant_id>')
def detail(restaurant_id):
    try:
        # IDに基づいてレストランを取得
        restaurant = Restaurant.get_by_id(restaurant_id)
    except:
        # レストランが見つからない場合は404エラー
        abort(404)
        
    return render_template('restaurant_details.html', title=restaurant.name, restaurant=restaurant)
