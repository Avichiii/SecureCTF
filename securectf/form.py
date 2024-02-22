from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField
from wtforms.validators import Length, Email, ValidationError, DataRequired, EqualTo, NumberRange

class Register(FlaskForm):

    username = StringField(validators=[Length(min=4, max=16), DataRequired()])
    email = EmailField(validators=[Email(), DataRequired()])
    password = PasswordField(validators=[Length(min=8), DataRequired()])
    confirm_password = PasswordField(validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='SignUp 🡪')

class Login(FlaskForm):

    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField(label='LogIn 🡪')

class Upload(FlaskForm):
    
    challenge_name = StringField(validators=[Length(min=5, max=24), DataRequired()])
    category = StringField(validators=[Length(max=24), DataRequired()])
    description = StringField(validators=[Length(max=60), DataRequired()])
    difficulty = StringField(validators=[Length(max=7), DataRequired()])
    points = IntegerField(validators=[NumberRange(min=20, max=500), DataRequired()])
    upload = SubmitField()