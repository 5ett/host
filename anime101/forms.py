from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, Length, EqualTo


class Login(FlaskForm):
    email = StringField('email', validators=[Email(), DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('login')


class Signup(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[
                             DataRequired(), Length(min=8, max=20)])
    confirm_pw = PasswordField('password', validators=[DataRequired(
    ), EqualTo(password, message="passwords don't match")])
    submit = SubmitField('sign up')
    submit = SubmitField('sign up')
