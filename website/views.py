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



@views.route('/add_album', methods=['POST', 'GET'])
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
            return redirect('/Albums')
        except:
            return "Error!"
    else:
        return render_template("createAlbum.html")

@views.route('/Albums/edit')
def edit_mode():
    albums = Album.query.order_by(Album.id).all()
    return render_template('albums_editor.html', Album=albums)


@views.route('/album/<int:id>/edit', methods=['POST', 'GET'])
def album_edit(id):
    album = Album.query.get(id)
    if request.method == 'POST':
        album.photo = request.form['photo']
        album.title = request.form['title']
        album.year = request.form['year']
        album.description = request.form['description']

        try:
            db.session.commit()
            return redirect('/Albums')
        except:
            return "Error!"
    else:

        return render_template("edit_album.html", album=album)


@views.route('/album/<int:id>/delete')
def delete_album(id):
    album = Album.query.get_or_404(id)
    try:
        db.session.delete(album)
        db.session.commit()
        return redirect('/Albums')
    except:
        return 'Error'


@views.route('/Albums')
def posts():
    albums = Album.query.order_by(Album.id).all()
    return render_template('albums.html', Album=albums)