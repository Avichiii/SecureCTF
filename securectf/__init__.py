from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '9b02d00476969f0e04ca626be846d4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///securectf.db'
db = SQLAlchemy(app)

from securectf import route
