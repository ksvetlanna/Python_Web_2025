#__call__ - экземпляр класса становится вызываемым (как функция)
# y = ax^2 + bx + c
class SquareFunction:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x ** 2 + self.b * x + self.c

s = SquareFunction(1,2,3)
print(s(2))