from anime101 import db, osyrus
from flask_login import UserMixin
from datetime import datetime


@osyrus.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    profile_photo = db.Column(db.String, nullable=False, default='unknown.jpg')
    notifier = db.Column(db.String, nullable=False, default='gon')
    sm_link_1 = db.Column(db.String)  # social media links and such
    sm_link_2 = db.Column(db.String)  # social media links and such
    posts = db.relationship('Article', backref='by', lazy=True)
    playlists = db.relationship('Playlist', backref='owned', lazy=True)
    facts = db.relationship('Fact', backref='submitted', lazy=True)
    like = db.relationship('Likes', backref='liked', lazy=True)
    comment = db.relationship('Comments', backref='commented', lazy=True)

    def __repr__(self):
        return f'User({self.username}, {self.email}, {self.sm_link_1}, {self.sm_link_2})'


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow())
    likes = db.Column(db.Integer)
    like = db.relationship('Likes', backref='upvoted', lazy=True)

    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'Article({self.title}, {self.date_posted}, {self.likes})'


class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titles = db.Column(db.String, nullable=False)
    cover_photo = db.Column(db.String, nullable=False, default='anime101.jpg')
    genre = db.Column(db.String, nullable=False)
    made_for = db.Column(db.String, nullable=False, default='everyone')
    likes = db.Column(db.Integer)
    marks = db.Column(db.Integer)
    comments = db.relationship('Comments', backref='playlist_comment')

    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'Playlist({self.id}, {self.titles}, {self.cover_photo},{self.owner})'


class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    # content lead would like to receive
    content = db.Column(db.String, nullable=False, default='all')
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
    liked = db.relationship('Likes', backref='liked_by', lazy=True)

    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'Fact({self.title}, {self.date_posted}, {self.owner.name})'


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(250), nullable=False)
    related = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False,
                     default=datetime.utcnow())  # date of comment
    fact = db.Column(db.Integer, db.ForeignKey('fact.id'))
    playlist = db.Column(db.Integer, db.ForeignKey('playlist.id'))

    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'Comment({self.id}, {self.comment}, {self.owner.name})'


class Likes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_liked = db.Column(db.String, nullable=False)
    post = db.Column(db.Integer, db.ForeignKey('article.id'))
    lists = db.Column(db.Integer, db.ForeignKey('playlist.id'))
    facts = db.Column(db.Integer, db.ForeignKey('fact.id'))

    thumbed_by = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'Like({self.id}, {self.liked_by.name}, {self.item_liked}'
