# ООП (encapsulation)
# Методы классов и анализ предыдущих вызовов
# Конструктор это метод

from lib import Car
car = Car('BMV','X5','black') # если ставится 2-е скобки то вызывается конструктор
#car.start_engine()
car.engine_on = True
car.drive_to('город')

car2 = Car() # если ставится 2-е скобки то вызывается конструктор
#car2.start_engine()
car2.drive_to('город')