# module.py
# Публичная функция
def greet(name):
    return f'Привет, {name}'


# Скрытая функция (we're all consenting adults here) если есть нижнее подчеркивание в названии функции то ее лучше не трогать
def _hidden_function():
    return 'Для внутреннего пользования'