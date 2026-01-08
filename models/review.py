from flask import Blueprint, render_template, request, redirect, url_for
from models import Review, Restaurant
from datetime import datetime

# Blueprintの作成
review_bp = Blueprint('review', __name__, url_prefix='/reviews')


# レビュー投稿（表示＋登録）
@review_bp.route('/', methods=['GET', 'POST'])
def review():
    # ======================
    # POST：レビュー登録
    # ======================
    if request.method == 'POST':
        restaurant_id = int(request.form['restaurant_id'])
        rating = int(request.form['rating'])
        age = int(request.form['age'])
        gender = request.form['gender']
        comment = request.form['comment']
        created_at = datetime.now()

        Review.create(
            restaurant=restaurant_id,
            rating=rating,
            age=age,
            gender=gender,
            comment=comment,
            created_at=created_at
        )

        # 登録後はトップへ戻す（または詳細画面でもOK）
        return redirect(url_for('index'))

    # ======================
    # GET：レビュー画面表示
    # ======================
    restaurants = Restaurant.select()

    return render_template(
        'review.html',
        restaurants=restaurants
    )
