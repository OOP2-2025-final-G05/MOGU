from flask import Blueprint, render_template, request, redirect, url_for
from models import Restaurant, Review
from peewee import fn

list_bp = Blueprint(
    'restaurant_list',
    __name__
)

@list_bp.route('/restaurant_list')
def restaurant_list():
    # ===== GETパラメータ（フィルター条件）=====
    # /restaurant_list?min_rating=3&address=東京
    min_rating = request.args.get('min_rating')  # 例: "3"
    address = request.args.get('address')        # 例: "東京"

    # ===== 基本：新しい順 =====
    restaurants = Restaurant.select().order_by(Restaurant.id.desc())

    items = []
    for r in restaurants:
        # 平均評価を計算（レビューが無ければ None）
        avg = (
            Review
            .select(fn.AVG(Review.rating))
            .where(Review.restaurant == r.id)
            .scalar()
        )
        avg_rating = round(avg, 1) if avg else None
        r.avg_rating = avg_rating if avg_rating is not None else '-'

        # ===== ★フィルター（○以上）=====
        if min_rating:
            try:
                min_rating_value = float(min_rating)
            except ValueError:
                min_rating_value = None

            if min_rating_value is not None:
                if avg_rating is None or avg_rating < min_rating_value:
                    continue

        # ===== 住所フィルター（部分一致）=====
        if address:
            # None対策（基本は入ってる想定だけど安全に）
            if not r.address or address not in r.address:
                continue

        items.append(r)

    return render_template(
        'restaurant_list.html',
        items=items,
        title='お店一覧',
        # テンプレ側でフィルター条件を保持するため渡す
        min_rating=int(min_rating) if (min_rating and min_rating.isdigit()) else None,
        address=address
    )

@list_bp.route('/restaurant_list_edit/<int:restaurant_id>', methods=['GET', 'POST'])
def restaurant_list_edit(restaurant_id):
    restaurant = Restaurant.get_or_none(Restaurant.id == restaurant_id)

    if restaurant is None:
        return redirect(url_for('restaurant_list.restaurant_list'))

    if request.method == 'POST':
        restaurant.name = request.form.get('name')
        restaurant.address = request.form.get('address')
        restaurant.genre = request.form.get('genre')
        restaurant.price = request.form.get('price')
        restaurant.time = request.form.get('time')
        restaurant.save()

        return redirect(url_for('restaurant_list.restaurant_list'))

    return render_template(
        'restaurant_list_edit.html',
        restaurant=restaurant,
        title='お店編集'
    )
