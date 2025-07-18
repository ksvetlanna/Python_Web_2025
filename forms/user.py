from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import SubmitField
from wtforms.fields.simple import EmailField, TextAreaField
from wtforms.validators import DataRequired

class Register(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired('Введите корректный e-mail')])
    password = PasswordField('Пароль', validators=[DataRequired('Пароль, обязательный к заполнению')])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired('Нужно подтвердить пароль')])
    name = StringField('Ваше имя', validators=[DataRequired('Введите ваше имя')])
    about = TextAreaField("Немного напишите про себя")
    submit = SubmitField("Регистрация")