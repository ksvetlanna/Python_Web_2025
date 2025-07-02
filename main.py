# Оператор is. если пишем a is b true будет только тогда, когда a и b один и тот же объект
my_refreg = ['колбаса','сыр','масло']
# his_refreg = ['колбаса','сыр','масло']
his_refreg=my_refreg  # если скопировать то нужно добавить .copy() иначе это ссылка на объект my_refreg
my_refreg +=['мясо']

print(his_refreg)
print(my_refreg is his_refreg)

print(my_refreg == his_refreg) # выдает true т.к. содержимое одинаковое
print(id(my_refreg) == id(his_refreg)) # выдает False совершенно разные объекты

temp = None
print(type(temp))
if temp is None:
    pass

# is говорит о том что и слева и справа один и тот же объект
# == мы сравниваем содержимое переменных, если is то сравниваем сами объекты


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