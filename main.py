# Функция, с переменным числом аргументов
# когда во входном параметре указана * то выведет кортеж
def multy(first, *args): # first позиционный аргумент, *args- переменное кол-во элементов
    #print(len(args)) # подсчет числа аргументов
    #print(args) # по индексу, либо перебором в цикле
    if not args:
        return first
    result = first
    for arg in args:
        result *= arg
    return result


def fio(name, surname):
    return f'{name} {surname}'

print(fio(name='Остап', surname='Бендер'))
print(multy(2,3,4,5))