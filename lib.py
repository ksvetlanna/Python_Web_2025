from unicodedata import unidata_version
from math import pi

class Student:
    def __init__(self, name='Bill', univ=''):
        # свойства (поля) класса
        self._name = name
        self._univercity = univ

    def get_univercity(self):
        return self._univercity


class Employee:
    def __init__(self, name='Bill', comp=''):
        # свойства (поля) класса
        self._name = name
        self._company = comp

    def get_company(self):
        return self._company


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.name ='круг'

    def perimetr(self):
        return  round(2 * pi * self.radius,2)

    def area(self):
        return pi * self.radius ** 2

    def get_name(self):
        return self.name


class Square:
    def __init__(self, side):
        self.side = side
        self.name = 'квадрат'

    def perimetr(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

    def get_name(self):
        return self.name

def shape_info(shape):
    print(f'Площадь: {shape.get_name()}а: {shape.area()}, Периметр: {shape.perimetr}')


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.name = 'прямоугольник'

    def perimetr(self):
        return  2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def get_name(self):
        return self.name

# для вывода названия
rect, c, sqr = ['прямоугольник', 'круг','квадрат']


def shape_info(shape: object):
    if isinstance(shape, Circle):
        fig = c
    elif isinstance(shape, Rectangle):
        fig = rect
    elif isinstance(shape, Square):
        fig = sqr
    print(f'Площадь: {fig}а: {shape.area()}, Периметр: {shape.perimetr}')


from itertools import count
class Clicker:
    def __init__(self):
        self._counter = 0

    def click(self):
        self._counter += 1

    def get_counter(self):
        return self._counter

    def reset(self):
        self._counter = 0


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
    counter = 0 # статичное свойство (счетчик машин)

    @property
    def __init__(self, brand='Noname', model='Noname', color='Noname'):
        self._brand = brand #'BMV'
        self.model = model #'X5'
        self.color = color #'black'
        self.engine_on = False
        Car.counter += 1
        # setters

    def start_engine(self):
        self.engine_on = True # self. - аналог глобальной переменной

    def drive_to(self, place):
        if self.engine_on:
            print(f'Едем в {place}, на {self.brand} {self.model}')
        else:
            print('Двигатель не заведен, не едем')


    @staticmethod
    def get_counter():
        return Car.counter




#print(__name__)

if __name__ != '__name__':
    print('Это библиотека, а исполняемый - main.py')