from flask import Blueprint, render_template
from models import Restaurant

list_bp = Blueprint(
    'restaurant_list',
    __name__
)

@list_bp.route('/restaurant_list')
def restaurant_list():
    items = Restaurant.select()

    return render_template(
        'restaurant_list.html',
        items=items,
        title='お店一覧'
    )
