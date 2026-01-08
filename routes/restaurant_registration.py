from flask import Blueprint, render_template, request, redirect, url_for
from models import Restaurant

# Blueprintの作成
reg_bp = Blueprint('res_reg', __name__, url_prefix='/restaurants')

@reg_bp.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        genre = request.form['genre']
        price = request.form['price']
        time = request.form['time']

        Restaurant.create(name=name, address=address, genre=genre, price=price, time=time)
        return redirect(url_for('res_reg.add'))
    return render_template('restaurant_registration.html')