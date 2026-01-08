from flask import Blueprint, render_template
from models import Restaurant, Review

# Blueprintの作成
details_bp = Blueprint('res_details', __name__, url_prefix='/restaurants')

@details_bp.route('/<int:restaurant_id>')
def details(restaurant_id):
    # 特定のお店を1件取得
    restaurant = Restaurant.get_or_none(Restaurant.id == restaurant_id)
    
    # そのお店に関連するレビューを取得
    reviews = Review.select().where(Review.restaurant == restaurant)
    
    return render_template(
        'restaurant_details.html',
        restaurant=restaurant,
        reviews=reviews
    )