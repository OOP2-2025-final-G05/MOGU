from flask import Flask, render_template
from models import initialize_database, Restaurant
from routes.restaurant_details import details_bp
from routes.restaurant_list import list_bp

app = Flask(__name__)
app.register_blueprint(details_bp)
app.register_blueprint(list_bp)

# データベースの初期化
initialize_database()

# トップページ
@app.route('/')
def index():
    return render_template('index.html')

# お店登録ページ
@app.route('/restaurant_registration')
def restaurant_registration():
    return render_template('restaurant_registration.html')

# レビューページ
@app.route('/review')
def review():
    return render_template('review.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
