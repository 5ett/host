from datetime import datetime
from anime101 import app, cerberus, db
from anime101.forms import Login, Signup
from flask import url_for, request, redirect, render_template, flash


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    form = Login()
    return render_template('login.html', form=form, title='Login')


@app.route('/signup')
def signup():
    form = Signup()
    return render_template('signup.html', form=form, title='Signup')


@app.route('/blog')
def blog():
    return render_template('blog.html', title='Blog')


@app.route('/factboard')
def factboard():
    return render_template('fact-board.html', title='Fact board')


@app.route('/playlists')
def playlists():
    return render_template('playlists.html', title='Playlists')
