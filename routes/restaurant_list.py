from flask import Blueprint, render_template
from models.restaurant_list import Restaurant

restaurant_list_bp = Blueprint(
    'restaurant_list',
    __name__
)

@restaurant_list_bp.route('/restaurant_list')
def restaurant_list():
    # 仮データなし（空リスト）
    items = []

    return render_template(
        'restaurant_list.html',
        items=items,
        title='お店一覧'
    )
