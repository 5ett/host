from datetime import datetime
from anime101 import app, cerberus, db
from anime101.forms import Login
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
    return render_template('signup.html', title='New User')
