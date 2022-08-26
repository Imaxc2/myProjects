from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    date = db.Column(db.DateTime, default=datetime.utcnow)

    title = db.Column(db.String(50), nullable=False)
    intro = db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Article {self.id}>'


@app.route("/")
def index():
    return render_template('main.html')


@app.route("/posts")
def posts():
    articles = Article.query.order_by(Article.date).all()
    return render_template('posts.html', articles=articles)


@app.route("/posts/<int:id>")
def post_detail(id):
    article = Article.query.get(id)
    return render_template('post-detail.html', article=article)


@app.route("/posts/<int:id>/delete")
def post_delete(id):
    articles = Article.query.get_or_404(id)

    try:
        db.session.delete(articles)
        db.session.commit()
        return redirect('/posts')
    finally:
        return redirect('/posts')


@app.route("/create", methods=["POST", "GET"])
def create():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:
            return 'Произошла ошибка'
    else:
        return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)
