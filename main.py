# Функция, с переменным числом аргументов
def sandwich(type_of_meal, with_onion=False, with_tomato=False):
    print('Булочка')
    if with_onion:
        print('Лук')
    print(type_of_meal)
    if with_tomato:
        print('Помидоры')
    print('Булочка')

sandwich('Котлета', with_onion=True)