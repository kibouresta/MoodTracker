from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moods.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Mood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mood_text = db.Column(db.String(256), nullable=False)

@app.route('/')
def index():
    moods = Mood.query.all()
    return render_template('index.html', moods=moods)

@app.route('/add', methods=['POST'])
def add_mood():
    mood_text = request.form['moodInput']  # フォームデータを取得
    new_mood = Mood(mood_text=mood_text)  # データベースエントリを作成
    db.session.add(new_mood)
    db.session.commit()  # データベースに保存
    return jsonify({'mood': mood_text})  # JSONレスポンスを返す

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # データベーステーブルを作成
    app.run(debug=True)
