# Файлы и ОС - модуль
import os

path = os.getcwd() # get current working directory
print(path)

os.chdir(path + '/images') #C:\Users\LCIMS2\PycharmProjects\SWE_PythonProject\images
print(os.getcwd())

os.chdir('..') #выйти на уровень выше
os.chdir(path + '/fonts')
print(os.getcwd()) #C:\Users\LCIMS2\PycharmProjects\SWE_PythonProject\fonts
#os.mkdir('libs')  будет создана директория

#os.makedirs('libs', exist_ok=True)  файл удаляется если он был. Мягкое создание директории. Вместо mkdir

if os.path.exists('libs'): #проверка существования пути
    os.rmdir('libs') #удаление директории