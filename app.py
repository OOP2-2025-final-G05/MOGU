from flask import Flask, render_template
from models import initialize_database, Restaurant
from routes.restaurant_registration import reg_bp 
from routes.restaurant_details import details_bp
from routes.restaurant_list import list_bp
from routes.review import review_bp

app = Flask(__name__)
app.register_blueprint(details_bp)
app.register_blueprint(list_bp)
app.register_blueprint(review_bp)

# データベースの初期化
initialize_database()

app.register_blueprint(reg_bp)

# トップページ
@app.route('/')
def index():
    return render_template('index.html')

# お店登録ページ
@app.route('/restaurant_registration')
def restaurant_registration():
    return render_template('restaurant_registration.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)