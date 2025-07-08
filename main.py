# Исключения (runtime)
from babel.plural import value_node

# try:
#   что пытаемся сделать
# except:
#   обрабатываем исключения
#else:
#   если исключения не было
#finally:
#   выполняется в любом случае

#Выводить ошибку пока не введут целове число не равно 0
print('Остаток от деления:')
loop = True # флаг
while loop:
    try:
        value = int(input('На что делим число 10:'))
        res = 10 % value
        print(f'Остаток от деления на 10 {value} = {res}')
    except ZeroDivisionError:
        print('На 0 делить нельзя!')
    except ValueError:
        print('Надо вводить только целые числа')
    except Exception as exp:
        print('Произошло исключение: ', exp.__class__.__name__, exp)
    else:
        loop = False
