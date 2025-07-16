# Введение во Flask
# В Terminal установить:
# pip install flask
# pip freeze > requirements.txt
# MVC- Model View Controller

from flask import Flask  # вызываем конструктор


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

if __name__ == '__main__': # запускаем
    app.run(host='localhost', port=5000, debug=debug)
