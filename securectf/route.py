from flask import render_template
from securectf import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/ctf')
def ctf():
    return render_template('ctf.html')

@app.route('/forum')
def forum():
    return render_template('forum.html')

@app.route('/community')
def community():
    return render_template('community.html')