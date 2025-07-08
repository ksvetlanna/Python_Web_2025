# Исключения (runtime)

# try:
#   что пытаемся сделать
# except:
#   обрабатываем исключения
#else:
#   если исключения не было
#finally:
#   выполняется в любом случае

# "бросаться исключениями" - raise
max_val = 10
min_val = 1

try:
    val = int(input(f'Введите целое число от {min_val} до {max_val}: '))
    if not min_val  < val < max_val:
        raise ValueError('введенное число вне диапазона')
    print(f'Введенное число: {val}, лежит в заданном диапазоне')
except ValueError as exp:
    print('Надо быть внимательнее:', exp)