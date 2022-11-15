from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.Text, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.id
