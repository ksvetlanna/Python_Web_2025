# Области видимости
square = 'Дворцовая площадь'

def square_area(length: int, width: int) -> None:
    '''

    :param Функуия вычисления площади:
    :param width:
    :return:
    '''

    area = length * width
    print(f'Площадь площади "{square}" = {area}')

def circle_length(radius):
    perimetr = 2 * PI * radius
    print(f'Длина окружности с радиусом {radius}={perimetr:.2f}') #.2f - это формат вывода, сколько после запятой

def print_array(array: list) -> None:
    for item in array:
        print(item)


words = ['Привет', 'мир']
PI = 3.14 # переменную можно ввести перед вызовом функции
print('Давай встретимся, на', square)
s = square_area(320 * 240)
print(s)
print('Ну что? Давай встретимся, на', square)
circle_length(5)



print_array(words)
print_array(['a','b','c'])
