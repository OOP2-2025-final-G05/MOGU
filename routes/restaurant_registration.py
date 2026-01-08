from flask import Blueprint, render_template, request, redirect, url_for
from models import Restaurant

# Blueprintの作成
reg_bp = Blueprint('res_reg', __name__, url_prefix='/restaurants')

@reg_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # フォームからデータを受け取って登録
        Restaurant.create(
            name=request.form['name'],
            address=request.form['address'],
            genre=request.form['genre'],
            min_price=int(request.form['min_price']),
            max_price=int(request.form['max_price']),
            opening_hours=request.form['opening_hours']
        )
        return redirect(url_for('res_list.list')) # 登録後、一覧へ飛ばす
    
    return render_template('restaurant_add.html', title='お店登録')

@reg_bp.route('/edit/<int:restaurant_id>', methods=['GET', 'POST'])
def edit(restaurant_id):
    # 既存データの取得と更新処理
    restaurant = Restaurant.get_or_none(Restaurant.id == restaurant_id)
    if request.method == 'POST':
        restaurant.name = request.form['name']
        restaurant.save()
        return redirect(url_for('res_list.list'))
    
    return render_template('restaurant_edit.html', restaurant=restaurant)