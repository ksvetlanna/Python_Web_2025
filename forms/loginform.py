#pip install flask-wtf
#pip freeze > requirements.txt

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Логин', validators=[DataRequired('Это обязательное поле')])
    password = PasswordField('Пароль', validators=[DataRequired('Это обязательное поле')])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')