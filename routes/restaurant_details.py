from flask import Blueprint, render_template, abort
from models import Restaurant, Review

# Blueprintの作成
details_bp = Blueprint('res_details', __name__, url_prefix='/restaurants')

@details_bp.route('/<int:restaurant_id>')
def restaurant_details(restaurant_id):
    restaurant = Restaurant.get_or_none(Restaurant.id == restaurant_id)
    if not restaurant:
        abort(404)
    return render_template('restaurant_details.html', restaurant=restaurant, title=restaurant.name)
