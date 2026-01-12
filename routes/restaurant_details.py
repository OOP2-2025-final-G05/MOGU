from flask import Blueprint, render_template, abort
from models import Restaurant, Review

# Blueprintの作成
details_bp = Blueprint('res_details', __name__, url_prefix='/restaurants')

@details_bp.route('/<int:restaurant_id>')
def restaurant_details(restaurant_id):
    restaurant = Restaurant.get_or_none(Restaurant.id == restaurant_id)
    if not restaurant:
        abort(404)
    
    # 追加：このお店に関連するレビューをすべて取得
    reviews = Review.select().where(Review.restaurant == restaurant_id).order_by(Review.created_at.desc())
    
    return render_template(
        'restaurant_details.html', 
        restaurant=restaurant, 
        title=restaurant.name,
        reviews=reviews  # テンプレートにレビューを渡す
    )