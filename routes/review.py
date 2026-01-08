from flask import Blueprint, request, redirect, url_for
from models import Review

# Blueprintの作成
review_bp = Blueprint('review', __name__, url_prefix='/reviews')

@review_bp.route('/add', methods=['POST'])
def add():
    # フォームから送られてきたレビュー情報を保存
    Review.create(
        restaurant=request.form['restaurant_id'],
        rating=int(request.form['rating']),
        comment=request.form['comment'],
        age=int(request.form['age']),
        gender=request.form['gender']
    )
    # 投稿後、そのお店の詳細画面に戻る
    return redirect(url_for('res_details.details', restaurant_id=request.form['restaurant_id']))