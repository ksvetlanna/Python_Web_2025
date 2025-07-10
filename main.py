# ООП (inheritance)
# класс, от которого наследуют: базовый, родительский или суперкласс
# класс, который наследуется: производным, дочерним
from math import pi
from abc import ABC, abstractmethod
from lib import shape_info


class Shape:  # Shape(object) - базовый класс
    def info(self):
        print(f'Класс:, {self.__class__.__name__}')

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

# Фигуры
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.name = 'круг'

    def perimetr(self):
        return round(2 * pi * self.radius, 2)

    def area(self):
        return round(pi * self.radius ** 2, 2)

    def get_name(self):
        return self.name

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.name = 'прямоугольник'

    def perimetr(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def get_name(self):
        return self.name


class Square(Rectangle): #Square стал дочерним классом, а Rectangle базовым(суперкласс)
    def __init__(self, side):
        # super(). - обращение к базовому классу (Rectangle)
        super().__init__(side, side) # вызываем __init__ из суперкласса Rectangle
        self.name = 'квадрат'

class Triangle(Square):
    def __init__(self, side):
        super().__init__(side)
        self.side = side
        self.name = 'треугольник'

    def area(self):
        return round((self.side ** 2 * 3 ** 0.5)/4,2)

    def perimetr(self):
        return self.side * 3

s = Square(5)
print(s.area())
print(s.perimetr())
print(s.get_name())


tr = Triangle(8)
print(tr.area())
print(tr.perimetr())
print(tr.get_name())
