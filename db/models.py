from . import db
from flask_login import UserMixin

class users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(30), nullable = False, unique = True)
    password =db.Column(db.String(162), nullable = False)

class articles(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    login_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(50), nullable = False)
    article_text = db.Column(db.Text, nullable = False)
    is_favorite = db.Column(db.Boolean)
    is_public=db.Column(db.Boolean, default=False)
    likes = db.Column(db.Integer)

class recipes(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    steps = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.String(300), nullable=True)