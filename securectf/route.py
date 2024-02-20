from flask import redirect, render_template, request, flash, url_for
from securectf import app, db
from securectf.form import Login, Register
from flask_login import login_user, logout_user, login_required, current_user
from securectf.models import Users

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = Register()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = Users.query.filter_by(username=form.username.data).first()
            
            if not user:
                user_signup = Users(
                    username=form.username.data,
                    email=form.email.data,
                    # password is setter function
                    password=form.password.data
                )
                
                db.session.add(user_signup)
                db.session.commit()
                login_user(user_signup)

                flash("User has been successfully registered!")
                return redirect(url_for('ctf'))
            
            else:
                flash('User Name already exists!')
                return redirect(url_for('signup'))
        
    if request.method == 'GET':
        return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if request.method == 'POST':
        if form.validate_on_submit():
            attempted_user = Users.query.filter_by(email=form.email.data).first()

            if attempted_user and attempted_user.check_password(attempted_password=form.password.data):
                login_user(attempted_user)
                flash("User has been successfully logged in!")
                return redirect(url_for('ctf'))
            
            return redirect(url_for('login'))
        
    if request.method == 'GET':
        return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('User has been logged out!')
    return redirect(url_for('home'))

@app.route('/ctf')
@login_required
def ctf():
    return render_template('ctf.html')

@app.route('/forum')
@login_required
def forum():
    return render_template('forum.html')

@app.route('/community')
@login_required
def community():
    return render_template('community.html')


@app.route('/users')
@login_required
def users():
    return render_template('userprofile.html')