# return vs yield

def generate_list():
    for i in range(5):               # return завершает функцию
        yield i                      # в данном случае yield это генерация, не завершает цикл

array = tuple(generate_list())        # нужно обязательно преобразовать либо в list - список, либо tuple - кортеж
print(array)