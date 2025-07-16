# Введение во Flask
# В Terminal установить:
# pip install flask
# pip freeze > requirements.txt
# MVC- Model View Controller
from fileinput import filename
from random import sample

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

if __name__ == '__main__': # запускаем
    app.run(host='localhost', port=5000, debug=debug)
