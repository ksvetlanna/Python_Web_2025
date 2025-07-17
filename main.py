# Введение во Flask
# В Terminal установить:
# pip install flask
# pip freeze > requirements.txt
# MVC- Model View Controller
# Get -запрашивает данные не меняя состояния сервера (read)
# Post - отправляет данные на сервер (submit)
# Put - заменяет все на сервере из контекста запроса ("заменить")
# Delete - удаляет указанные данные
# Patch - частичное изменение даннах
# шаблонизатор Jinja
from fileinput import filename
from http.client import responses
from random import sample
import os.path


#------------------------------------------------------------------------------------------------------------------
from flask import Flask, url_for, request, render_template  # вызываем конструктор
from werkzeug.utils import secure_filename
import sqlite3



app = Flask(__name__) # на локальном компьютере запустится для отладки скрипта
app.config['UPLOAD_FOLDER'] = 'uploads/'     #директория куда сохраняем, слева в дереве
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'zip', 'jpg', 'png']    # расширения которые мы разрешаем для загрузки
debug = False         # сделать true если нужно проверить

def allowed_file(filename):   #проверка на корректность файла
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS       # для переноса каретки используем скобки


@app.route('/')         # декоратор смотрит какой путь набрали,
def index():
    username = 'слушатель'
    params = {}
    params['user'] = 'слушатель'
    params['title'] = 'приветствие'
    params['weather'] = 'Сегодня хорошая погода'
    return render_template('index.html',
                           **params)
# проверить что выводит http://localhost:5000/index


@app.route('/about')
def about():
    print('Вызвана функция about')
    return render_template('about.html', title='О нас')
# проверить что выводит http://localhost:5000/about

@app.route('/contacts')
def contacts():
    print('Вызвана функция contacts')
    return render_template('contacts.html', title='Контакты')


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

@app.route('/form-test', methods=['POST', 'GET'])
def form_test():
    if request.method == 'GET':
        with open('form.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['level'])
        print(request.form['about'])
        print(request.form['gender'])
        print(request.form['accept'])

        return 'Форма успешно отправлена'

# для загрузки файла
#C:\Users\LCIMS2\PycharmProjects\SWE_PythonProject\old\images
@app.route('/upload', methods=['POST', 'GET'])
def file_upload():
    if request.method == 'GET':
        with open('upload.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        # print(request.files)
        if 'file' not in request.files:
            return 'Файл не был выбран!!!'

        file = request.files['file']       # пишем имя кот. указали в name

        if file.filename == '':            # если название файла пустое
            return 'Файл не был выбран!!!'

        if file and allowed_file(file.filename):
            new_name = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_name))
            return f'Файл {new_name} успешно загружен!'
    return "Ошибка загрузки"


@app.route('/numbers')
@app.route('/numbers/<int:num>')
def odd_even(num=None):
    if num is None:
        return render_template('numbers.html',
                           title='Нет числа', number='')
    return render_template('numbers.html',
                           title='Нет числа', number=num)

@app.route('/deals')
def printlist():
    deal = ['Помыть посуду','Выгулять собаку','Помыть посуду','Погулять']
    return render_template('printlist.html',
                            deals=deal)



@app.route('/queue')
def queue():
    #loop.index номер итерации начиная с 1
    # loop.index0 номер итерации начиная с 0
    # loop.first True, если первая итерация
    # loop.last True, если последняя итерация
    return render_template('vars.html', title='стоим в очереди')

if __name__ == '__main__': # запускаем
    app.run(host='localhost', port=5000, debug=debug)
