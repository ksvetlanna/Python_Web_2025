class Person:
    def __init__(self, name='Bill', age=1):
        self._name = name    #self.name атрибут кот. будет отражать свойство, поле класса
        self._age = age

    # setters не использовать пустые имена
    def set_name(self, new_name):
        if new_name:
            self._name = new_name

    def set_age(self, new_age):
        if 0 < new_age <150:
            self._age = new_age
        else:
            print('Некорректный возраст -', new_age)
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age


    def person_info(self):
        print(f'Челове с именем {self._name}. Возраст: {self._age}')


class Car:
    def __init__(self, brand='Noname', model='Noname', color='Noname'):
        self.brand = brand #'BMV'
        self.model = model #'X5'
        self.color = color #'black'
        self.engine_on = False

    def start_engine(self):
        self.engine_on = True # self. - аналог глобальной переменной

    def drive_to(self, place):
        if self.engine_on:
            print(f'Едем в {place}, на {self.brand} {self.model}')
        else:
            print('Двигатель не заведен, не едем')

def summ(a, b):
    return a + b


def diff(a, b):
    return a - b

#print(__name__)

if __name__ != '__name__':
    print('Это библиотека, а исполняемый - main.py')