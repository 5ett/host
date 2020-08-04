from datetime import datetime
from anime101.other_funcs import cap
from anime101 import app, cerberus, db
from anime101.forms import Login, Signup
from anime101.models import User
from flask import url_for, request, redirect, render_template, flash
from flask_login import current_user, login_user, login_user, current_user


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    form = Login()
    if form.validate_on_submit():
        user_check = User.query.filter_by(email=form.email.data).first()
        if user_check and cerberus.check_password_hash(user_check.password, form.password.data):
            login_user(user_check)
        else:
            flash('invalid credentials', 'danger')

    return render_template('login.html', form=form, title='Login')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = Signup()
    if form.validate_on_submit():
        passwd = cerberus.generate_password_hash(
            form.password.data).decode('utf8')
        full_name = cap(f'{form.first_name.data} {form.last_name.data}')
        new_user = User(name=full_name, username=form.username.data,
                        email=form.email.data, password=passwd)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('confirm'))
    return render_template('signup.html', form=form, title='Signup')


@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
    flash("you've succesfully become a Hunter", 'success')
    user_profile_photo = url_for(
        'static', filename='media/profile_photos/' + current_user.profile_photo)
    return render_template('confirm.html', title='Anime101', user_profile_photo=user_profile_photo)


@app.route('/blog')
def blog():
    user_profile_photo = url_for(
        'static', filename='media/profile_photos/' + current_user.profile_photo)
    return render_template('blog.html', title='Blog', user_profile_photo=user_profile_photo)


@app.route('/factboard')
def factboard():
    user_profile_photo = url_for(
        'static', filename='media/profile_photos/' + current_user.profile_photo)
    return render_template('fact-board.html', title='Fact board', user_profile_photo=user_profile_photo)


@app.route('/playlists')
def playlists():
    user_profile_photo = url_for(
        'static', filename='media/profile_photos/' + current_user.profile_photo)
    return render_template('playlists.html', title='Playlists', user_profile_photo=user_profile_photo)
