# ООП (inheritance)
# класс, от которого наследуют: базовый, родительский или суперкласс
# класс, который наследуется: производным, дочерним
class Rectangle:
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

s = Square(5)
print(s.area())
print(s.perimetr())
print(s.get_name())