from flask import Flask, render_template

app = Flask(__name__)

# トップページ
@app.route('/')
def index():
    return render_template('index.html')

# お店登録ページ
@app.route('/restaurant_registration')
def restaurant_registration():
    return render_template('restaurant_registration.html')

# お店一覧ページ
@app.route('/restaurant_list')
def restaurant_list():
    return render_template('restaurant_list.html')

# レビューページ
@app.route('/review')
def review():
    return render_template('review.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
