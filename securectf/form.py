from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import Length, Email, ValidationError, DataRequired, EqualTo

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