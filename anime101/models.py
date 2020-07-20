from anime101 import db
from flask_login import UserMixin
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    profile_photo = db.Column(db.String, nullable=False, default='unknown.jpg')
    notifier = db.Column(db.String, nullable=False, default='gon.png')
    sm_link_1 = db.Column(db.String)  # social media links and such
    sm_link_2 = db.Column(db.String)  # social media links and such
    posts = db.relationship('Article', backref='by', lazy=True)
    playlists = db.relationship('Playlist', backref='owned', lazy=True)

    def __repr__(self):
        return f'User({self.username}, {self.email}, {self.sm_link_1}, {self.sm_link_2})'


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow())
    likes = db.Column(db.Integer)
    owner = db.Column(db.Integer, db.ForeignKey('user'), nullable=False)

    def __repr__(self):
        return f'Article({self.title}, {self.date_posted}, {self.likes})'


class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titles = db.Column(db.String, nullable=False)
    cover_photo = db.Column(db.String, nullable=False, default='anime101.jpg')
    genre = db.Column(db.String, nullable=False)
    likes = db.Column(db.Integer)
    marks = db.Column(db.Integer)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comments', backref='playlist_comment')

    def __repr__(self):
        return f'Playlist({self.id}, {self.titles}, {self.cover_photo},{self.owner})'


class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    content = db.Column(db.String, nullable=False, default='all')  # content lead would like to receive
    date_added = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow())

    def __repr__(self):
        return f'Lead({self.email}, {self.content}, {self.date_added})'


class Fact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow())
    likes = db.Column(db.Integer)
    comments = db.relationship('Comments', backref='fact_comment', lazy=True)


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(250), nullable=False)
    related = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False,
                     default=datetime.utcnow())  # date of comment
    fact = db.Column(db.Integer, db.ForeignKey('fact.id'))
    playlist = db.Column(db.Integer, db.ForeignKey('playlist.id'))
