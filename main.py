# Функции
# Scope (local or global)
# Синтаксис:
# def <имя функции> ([параметры]):
#     команды
person = 'Пётр'   # глобальная переменная
count = 0

def greet_to_name(name='noname'):
    print('Привет,',name)

def increment():
    global count # что бы поменять значение глобальной переменной
    count += 1

def print_list(array=None):
    if array is None:
        array = []
    for item in array:
        print(item)

# перед вызовом функции и ее объявлением нужны два enter
# Функция не имеет памяти,
# в функцию передается копия самой переменную (речь идет о глобальных переменных)
greet_to_name(person) # вызов функции
#increment()


