# Декораторы
import time
from turtledemo.penrose import start


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f'Функция исполнялась:{finish - start:.4f} сек.')
        return result
    return wrapper

@timeit
def test():
    time.sleep(0.8)

test()
#--------------------------------------------------------------------------------------------
'''def logger(func):
    counter = 0
    def decorated_func(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(counter, '->', 'Аргументы:', args, 'Именованные аргументы:', kwargs)
        result = func(*args, **kwargs)
        print('____', 'Результат:', result)
        return result
    return decorated_func

@logger
def make_burger(meal='говядиной', onion=False, tomato=False):
    print('Булочка')
    if onion:
        print('Луковые кольца')
    print('Котлета с', meal)
    if tomato:
        print('Помидоры')
    print('Булочка')
make_burger('бараниной', onion=True)'''

#--------------------------------------------------------------------------------------------
'''def outher():
    x = 5

    def inner():
        nonlocal x
        print('Nonlocal x=', x)
        x = 10
    inner()
    print('New x=', x)

outher()'''

#--------------------------------------------------------------------------------------------
# Декораторы
# Выводит большими буквами сообщение
'''def upper_case_print(old_func):
    def new_func(*args, **kwargs):
        case = kwargs.pop('case', None)
        if case == 'U':
            args = [str(arg).upper() for arg in args]
        if case == 'L':
            args = [str(arg).lower() for arg in args]
        return old_func(*args, **kwargs)
    return new_func
new_print = upper_case_print(print)
new_print('Привет, Пока')
new_print('Привет, Пока', case='U')'''