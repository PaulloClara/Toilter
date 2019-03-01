from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
  username = StringField('username', validators=[DataRequired()])
  password = PasswordField('password', validators=[DataRequired()])
  rememberMe = BooleanField('rememberMe')


class RegisterForm(FlaskForm):
  username = StringField('username', validators=[DataRequired()])
  name = StringField('name', validators=[DataRequired()])
  password = PasswordField('password', validators=[DataRequired()])
  email = StringField('email', validators=[DataRequired()])
  