from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Flaskアプリケーションの設定
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moods.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'super_secret_key'

db = SQLAlchemy(app)

# データベースモデル
class Mood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mood_text = db.Column(db.String(256), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, nullable=True)  # user_idをNULL許可に変更

# トップページ
@app.route('/')
def index():
    moods = Mood.query.order_by(Mood.timestamp.desc()).all()
    return render_template('index.html', moods=moods)

# 気分を追加
@app.route('/add', methods=['POST'])
def add_mood():
    mood_text = request.form['moodInput']
    # 仮のuser_idを設定（ログインしている場合にはsession['user_id']を使用）
    user_id = session.get('user_id', None)
    new_mood = Mood(mood_text=mood_text, user_id=user_id)
    db.session.add(new_mood)
    db.session.commit()
    return jsonify({'mood': mood_text, 'timestamp': new_mood.timestamp.strftime('%Y-%m-%d %H:%M:%S')})

# アプリケーションの実行
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
