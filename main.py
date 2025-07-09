# ООП (encapsulation)
# Геттеры и сеттеры
'''class Person:
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
'''
from  lib import Person

p = Person()  #вызов конструктора
p.set_age(7897)
p.person_info()