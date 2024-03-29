from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '9b02d00476969f0e04ca626be846d4'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///securectf.db'
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

bcrypt = Bcrypt(app)

from securectf import route
