from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from .models import Album
from . import db

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@login_required
def home():
    return render_template("home.html", name=current_user.username)

@views.route('/Create-Albums')
def create_albums():
    return render_template('CreateAlbum.html', name=current_user.username)

@views.route('', methods=['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        photo = request.form['photo']
        title = request.form['title']
        year = request.form['year']
        description = request.form['description']

        album = Album(photo=photo, title=title, year=year, description=description)
        try:
            db.session.add(album)
            db.session.commit()
            return redirect('/post')
        except:
            return "Помилка!"
        else:
            return render_template("CreateAlbum.html")


@views.route('/posts')
def posts():
    articles = Album.query.order_by(Album.date).all()
    return render_template('Albums.html', Album=Album)