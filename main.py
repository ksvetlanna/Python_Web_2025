# ООП (polymorphism)
from math import hypot

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'<Point: ({self.x}, {self.y})>' #объект пишется в угловых скобках < ... >

    def __repr__(self):
        return f'<List of Points: ({self.x}, {self.y})>' # если сложный список обектов то __repr__

    def __sub__(self, other):
        return Point(abs(self.x - other.x), abs(self.y - other.y)) # abs абсолютная величина

    def __add__(self, other):
        return hypot(self.x - other.xЫзусшфд , self.y - other.y)

p1 = Point(5,4)
p2 = Point(10, 2)
print(p1 - p2)
print(p1 + p2)

'''from idlelib.configdialog import is_int

lst = list(range(1, 15))
lst += ['a']

class Stat:
    def __init__(self, vals):
        self.values = vals[:]  # получаем копию

    def is_all_int(self) -> bool:
        return all(isinstance(item, int) for item in self.values)

    def get_min(self):
        if self.is_all_int():
            return min(self.values)
        return None

    def get_max(self):
        if self.is_all_int():
            return max(self.values)
        return None

    def get_aver(self):
        if self.is_all_int():
            return sum(self.values) / len(self.values)
        return None


s = Stat(lst)
print(s.get_min())
print(s.get_max())
print(s.get_aver())
'''
'''class Selector:
    def __init__(self, vals):
        self.values = vals[:]  # получаем копию списочного выражения, что бы не испортить рабочий вариант

    def get_odd(self):
        return [x for x in self.values if x % 2 == 1]

    def get_even(self):
        return [x for x in self.values if x % 2 == 0]

s = Selector(lst)
print(s.get_odd())
print(s.get_even())
print(lst)'''
'''from lib import Student, Employee, Person

people = [
    Person('Александр', 27),
    Student('Дмитрий', 'ГУАП'),
    Employee('Петр','Авангард')
]

for person in people:
    if isinstance(person, Student):
        print(person.get_univercity())
    elif isinstance(person, Employee):
        print(person.get_company())
    else:
        print(person.get_name())'''
# ------------------------------------------------------------------------------------------------
'''class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author
        
    def get_title(self):
        return self._title
        
    def get_author(self):
        return self._author

from lib import Book
book = Book('Язык С++', 'Бьярн Страупструп')
print(f'{book.get_title(), book.get_author()}')'''


   #------------------------------------------------------------------------------------------------

'''    
print(1 + 2) # оператор + является полиморфным будет int
print(1 + 2.0) # оператор + является полиморфным будет float
print('abc' + 'def') # оператор + является полиморфным будет str
print([1,2] + [3,4]) # список [1,2,3,4]

def func(x, y):
    return x + y
print(func(2,3.0))'''