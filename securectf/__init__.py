from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '9b02d00476969f0e04ca626be846d4'

from securectf import route
