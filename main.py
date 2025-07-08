# Задача 1

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
try:
    index = int(input('Введите индекс: '))
    if not -len(lst) < index < len(lst) - 1:
        raise ValueError('Индекс вне диапазона')
    res = lst[index]
    print(f'Число по индексу {index}: {res}')
except ValueError as exp:
    mess = exp.args
    if mess[0].startswith('invalid literal'):
        print(f'Вводить надо числа')
    else:
        print(exp)