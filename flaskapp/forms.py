from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskapp.models import User

# ////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////// SIGNUP FORM //////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    full_name = StringField('Fullname', validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

# ////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////// LOGIN FORM ///////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# ////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////// ADD POST FORM ////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////


class CreatePostForm(FlaskForm):
    caption = TextAreaField('Caption', validators=[DataRequired()])
    submit = SubmitField('Post')
