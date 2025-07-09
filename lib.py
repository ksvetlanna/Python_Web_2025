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