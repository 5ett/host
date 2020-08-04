from flask_wtf import FlaskForm
from anime101.models import User
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, Length, EqualTo, ValidationError


class Login(FlaskForm):
    email = StringField('email', validators=[Email(), DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('login')

    def validate_email(self, email):
        user_verification = User.query.filter_by(email=email.data).first()
        if not user_verification:
            raise ValidationError("user doesn't exist")


class Signup(FlaskForm):
    first_name = StringField('first name', validators=[DataRequired()])
    last_name = StringField('last name', validators=[DataRequired()])
    username = StringField('username', validators=[
                           DataRequired(), Length(min=8, max=20)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[
                             DataRequired(), Length(min=8)])

    confirm = PasswordField('confirm password', validators=[
                            DataRequired(), EqualTo('password', message="passwords don't match")])

    submit = SubmitField('sign up')

    # def validate_username(self, username):
    #     if username.errors:
    #         raise ValidationError('username should 8 characters at least')

    # def validate_email(self, email):
    #     if email.errors:
    #         raise ValidationError('make sure the email you entered is correct')

    # def validate_password(self, password):
    #     if password.errors:
    #         raise ValidationError('password should be at least 8 characters long')

    # def validate_confirm(self, confirm):
    #     if confirm_pw.errors:
    #         raise ValidationError('make sure the passwords match')
