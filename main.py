# Введение во Flask
# В Terminal установить:
# pip install flask
# pip freeze > requirements.txt
# MVC- Model View Controller
from fileinput import filename
from http.client import responses
from random import sample
import sqlite3

#------------------------------------------------------------------------------------------------------------------
from flask import Flask, url_for  # вызываем конструктор


app = Flask(__name__) # на локальном компьютере запустится для отладки скрипта
debug = False         # сделать true если нужно проверить

@app.route('/')         # декоратор смотрит какой путь набрали,
@app.route('/index')
def index():
    return 'Привет, Flask'
# проверить что выводит http://localhost:5000/index


@app.route('/about')
def about():
    print('Вызвана функция about')
    return 'О нас'
# проверить что выводит http://localhost:5000/about


@app.route('/countdown')
def countdown():
    lst = [str(x) for x in reversed(range(10))] # сделали обратный отсчет от 10 ... 0
    lst.append('Полетели!!!')
    return '<br>'.join(lst)    #<br> и спользуем в качестве объединителя, возвращает только СТРОКУ
# проверить что выводит http://localhost:5000/countdown


@app.route('/image')    # для изображений, файлов скриптов java (должно хранится в спец файле)
                        # обязательно для обработки этих файлов нужна папка static
def show_image():
    return f'<img src="{url_for('static', filename='images/python6.jpg')}">'
    # все лежит в static, а файл в директории images/python6.jpg


@app.route('/sample-page')
def sample_page():
    return f"""
            <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>Картинка змейки</title>
        </head>
        <body>
            <img src="{url_for('static', filename='images/python6.jpg')}" alt="Python">
        </body>
        </html> 
            """

@app.route('/sample-page2')            # прочитали файл в вывели в строку
def sample_page2():
    with open('temp.html','r', encoding='utf-8') as html:
        return html.read()

# типы конвектора: по умолчанию <string>
# <int:number> целое число
# <float:number> дробь, вещественные числа
# <path:p> может содержать слэши для указания пути
# <uuid:id> строка-идентификатор  (пример - 54610465па4552-ывп263)  содержит 16 байт в 16ричном формате
@app.route('/greeting/<user>/<int:id_num>') #<user> будет воспринимать как информацию для функции поле user
def greeting(user, id_num):
    return f'Привет, {user} с id={id_num}'

# подключились к БД, для проверки загрузить http://localhost:5000/get-user/17
@app.route('/get-user/')      # обработка ошибки, если пользователь ничего не ввел в параметр
@app.route('/get-user/<int:id_num>')
def get_user(id_num=None):
    if id_num is None:
        return 'Нет номера записи'
    conn = sqlite3.connect('db/movies.sqlite') # подключаемся к БД
    cur = conn.cursor()
    query = f'select name, city from dz_users where trip_id={id_num}' # выполняем запрос
    response = cur.execute(query)
    result = response.fetchone()
    name, city = result
    #print(result)
    cur.close()
    conn.close()
    return f'''<table border="1">
    <tr>
    <td>ФИО</td>
    <td>Город</td>
    </tr>
    <tr>
    <td>{name}</td>
    <td>{city}</td>
    </tr>
    </table>'''

if __name__ == '__main__': # запускаем
    app.run(host='localhost', port=5000, debug=debug)
