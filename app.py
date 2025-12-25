from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# 仮でボタンリンク用のルートも作っておく
@app.route('/add_shop')
def add_shop():
    return "<h2>お店登録ページ（まだフォームなし）</h2>"

@app.route('/shop_list')
def shop_list():
    return "<h2>お店一覧ページ（まだデータなし）</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
