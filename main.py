from PIL import Image # базовые манипуляции с изображением

image = Image.open('images/Python.jpg') # файл лежит в папке images это видно в дереве

x,y = image.size # распаковываем файл в переменные ширину и длину
mode = image.mode
pixels = image.load() # загрузка таблицы пикселей

print(f'Ширина ={x}, высота = {y}')
print(f'Цветовая схема: {mode}')

resized = image.resize((400, 300)) # уменьшить размер изображения
resized.save('images/python8.jpg') # пересохранить файл с новым именем
