# Оператор is. если пишем a is b true будет только тогда, когда a и b один и тот же объект
#словари как и множества со списками изменяемые объекты
#Пример 1 создаем новый объект
a = 1
print(id(a))
a += 1
print(id(a)) # создан объект с новым содержимым

#Пример 2 тут объект один и тот же
b = [0]
print(id(b))
b[0] += 1
print(id(b)) # создан объект с новым содержимым

c ={'a': 1}
print(id(c))
c['a'] += 1
print(id(c))


'''def print_goodbye(arg:):
    print('goodbye', end=' ')

def print_cruel(arg:):
    print('cruel', end=' ')

def print_world(arg:):
    print('world', end=' ')


def main():
a = print_goodbye(1)
b = print_cruel(2)
c = print_world(3)


main()'''