# Задача 2
# Перепимсать 1ый вариант программы на исключения try

'''#пример решения задачи без try
while True:
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')

    if a.isdigit() and b.isdigit():
        if int(b) == 0:
            print('На ноль делить нельзя')
        else:
            print(int(a) / int(b))
            break
    else:
        print('Вводить надо только числа.')
'''

# решение
while True:
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    try:
        result = int(a) / int(b)
    except ZeroDivisionError:
        print('На ноль делить нельзя!!!')
    except ValueError:
        print('Нужно вводить числа ...')
        print(f'А введено {a} и {b} :(')
    else:
        print(result)
        break