from flask import Blueprint, render_template, request, redirect, url_for
from models import Restaurant, Review
from peewee import fn

list_bp = Blueprint(
    'restaurant_list',
    __name__
)

@list_bp.route('/restaurant_list')
def restaurant_list():
    restaurants = Restaurant.select()
    
    # Calculate average ratings and attach to each restaurant
    items = []
    for r in restaurants:
        # Calculate average rating from reviews
        avg = Review.select(fn.AVG(Review.rating)).where(Review.restaurant == r.id).scalar()
        r.avg_rating = round(avg, 1) if avg else '-'
        items.append(r)

    return render_template(
        'restaurant_list.html',
        items=items,
        title='お店一覧'
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
