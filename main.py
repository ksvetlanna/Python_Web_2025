# Внешние библиотеки
# Графика
# PIL - Python Imagine Library
# pip freeze > requirements.txt - созданеие файла зависимостей
# pip install -r  requirements.txt - установка списка библиотек
# RGB каждый из цветов меняется. есть место пикселя и его цвет
# thumbnail
from PIL import Image #базовые манипуляции с изображением

image = Image.open('images/Python.jpg') # файл лежит в папке images это видно в дереве

x,y = image.size # распаковываем файл в переменные ширину и длину
mode = image.mode
pixels = image.load() # загрузка таблицы пикселей


print(f'Ширина ={x}, высота = {y}')
print(f'Цветовая схема: {mode}')

#1 image_rotate = image.rotate(90) #поворот объектра (картинки)
#1 image_rotate.save('images/python5.jpg') # пересохранить файл с новым именем

#2 image_flip = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT) #горизонтальное отражение (зеркально)
#2 image_flip.save('images/python6.jpg') # пересохранить файл с новым именем

image_cropped = image.crop((250, 100, 300, 500))
image_cropped.save('images/python7.jpg') # пересохранить файл с новым именем
#---------------------------------------------------------------------------------------------------------
'''# оттенки серого
from PIL import Image #базовые манипуляции с изображением

image = Image.open('images/Python.jpg') # файл лежит в папке images это видно в дереве

x,y = image.size # распаковываем файл в переменные ширину и длину
mode = image.mode
pixels = image.load() # загрузка таблицы пикселей


print(f'Ширина ={x}, высота = {y}')
print(f'Цветовая схема: {mode}')

for i in range(x): # пошли по пикселям по ширине
    for j in range(y):
        r, g, b = pixels[i, j]
        average = (r+g+b) // 3
        pixels[i, j] =  average, average, average

image.save('images/python4.jpg') # пересохранить файл с новым именем
'''
#-----------------------------------------------------------------------------------------------------
#Негатив
'''
from PIL import Image #базовые манипуляции с изображением

image = Image.open('images/Python.jpg') # файл лежит в папке images это видно в дереве

x,y = image.size # распаковываем файл в переменные ширину и длину
mode = image.mode
pixels = image.load() # загрузка таблицы пикселей


print(f'Ширина ={x}, высота = {y}')
print(f'Цветовая схема: {mode}')

for i in range(x): # пошли по пикселям по ширине
    for j in range(y):
        r, g, b = pixels[i, j]
        pixels[i, j] = 255 - g, 255 - r, 255 - b

image.save('images/python3.jpg') # пересохранить файл с новым именем
'''
#-----------------------------------------------------------------------------------------------------
'''from PIL import Image #базовые манипуляции с изображением

image = Image.open('images/Python.jpg') # файл лежит в папке images это видно в дереве

x,y = image.size # распаковываем файл в переменные ширину и длину
mode = image.mode
pixels = image.load() # загрузка таблицы пикселей


print(f'Ширина ={x}, высота = {y}')
print(f'Цветовая схема: {mode}')

for i in range(x): # пошли по пикселям по ширине
    for j in range(y):
        r, g, b = pixels[i, j]
        pixels[i, j] = g, r, b
image.save('images/python2.jpg') # пересохранить файл с новым именем
'''