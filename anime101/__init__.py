from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '56a11abbfda7b24dff5d5e7975439780'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anime101.db'
db = SQLAlchemy(app)
cerberus = Bcrypt(app)

from anime101 import routes
