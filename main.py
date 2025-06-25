# Формат вывода 2

name = 'Игорь'
email = 'igor@mail.ru'
age = 32
weight=92.93

#1 способ (метод плейсхолдеры)
# %s-string
# %d-string
# %f-float
print('Имя: %s, E-mail: %s, Возраст: %d' % (name, email, age))


#2 способ
print('Имя: {}, E-mail: {}, Возраст: {}' .format (name, email, age))

#3 способ есть только с версии python 3.6
print(f'Имя: {name}, E-mail: {email}, Возраст: {age}, Вес: {weight:.2f}')
#2f-количество знаков после запятой