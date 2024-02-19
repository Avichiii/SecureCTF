from securectf import db
from flask_login import UserMixin

# connector table for users / ctfchallenges
ctfuser = db.Table('ctfuser',
    db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
    db.Column('ctf_id', db.Integer(), db.ForeignKey('ctf.id'))
)

# users tables
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(length=50), nullable=False)
    completed_challenges = db.relationship('Ctf', secondary=ctfuser, backref='pawned_challenges', lazy=True)


    def __str__(self) -> str:
        return f'User: {self.username}'
    
class UserProperties(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    bio = db.Column(db.String(length=200), default="User's bio")
    level = db.Column(db.Integer(), nullable=False)
    # profile_picture = db.Column(db.String(length=200), default='')
    rank = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

class UsersSocial(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    linkedin = db.Column(db.String(length=100))
    github = db.Column(db.String(length=100))
    youtube = db.Column(db.String(length=100))
    website = db.Column(db.String(length=100))
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

# challenges table
class Ctf(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    challenge_name = db.Column(db.String(length=20), nullable=False, unique=True)
    points = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.Integer(), nullable=False)
    uploaded_user = db.Column(db.String(length=50), unique=True, nullable=False)

    def __str__(self) -> str:
        return f'Challenge: {self.challenge_name}'
    
# category table
class Category(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    category_name = db.Column(db.String(length=50), nullable=False, unique=True)
    challenge_id = db.Column(db.Integer(),  db.ForeignKey('ctf.id'))

# forum table
class Forum(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    message = db.Column(db.String(length=500))
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

# community table
class Community(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    header = db.Column(db.String(length=100), nullable=False, unique=True)
    link = db.Column(db.String(length=200), nullable=False)
    username = db.Column(db.Integer(), db.ForeignKey('users.id'))
    challenge=  db.Column(db.Integer(), db.ForeignKey('ctf.id'))