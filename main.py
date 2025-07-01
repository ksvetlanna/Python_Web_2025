# Функции
# Return Value

# чистая функция не преобразовывает входные данные, т.е. оставляет их без изменения
# пример чистой функции
def square(num):
    return num ** 2

def even_odd(num):
    if num % 2 == 0: # если условие не выполнится, то сразу напечатает нечётное и выйдет
        return 'Чётное'
    return 'Нечётное'

def print_string(s=None):
    if s is None:
       return
    print(s)


t = square(5)
print(even_odd(5))
print(t)