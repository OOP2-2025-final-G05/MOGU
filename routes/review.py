from flask import Blueprint, render_template, request, redirect, url_for
from models import Review, Restaurant
from datetime import datetime

review_bp = Blueprint('review', __name__, url_prefix='/reviews')

@review_bp.route('/', methods=['GET', 'POST'])
def review():
    restaurants = Restaurant.select()
    selected_id = request.args.get('restaurant_id')

    if request.method == 'POST':
        restaurant_id = int(request.form['restaurant_id'])
        rating = int(request.form['rating'])
        comment = request.form['comment']
        age = int(request.form['age'])
        gender = request.form['gender']

        Review.create(
            restaurant=restaurant_id,
            rating=rating,
            comment=comment,
            age=age,
            gender=gender,
            created_at=datetime.now()
        )

        return redirect(url_for('restaurant_list.restaurant_list'))

    return render_template(
        'review.html',
        restaurants=restaurants,
        selected_id=selected_id
    )
