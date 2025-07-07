# Внешние библиотеки
# Графика
# PIL - Python Imagine Library
# pip freeze > requirements.txt - создание файла зависимости
# pip install -r requirements.txt - установка списка библиотек
from PIL import Image, ImageDraw, ImageFont

# https://fontsforyou.com/ru/specific-fonts/ttf-fonts/languageru   можно скачать любой шрифт, шрифт должен быть ТОЛЬКО .ttf, скаченный файл переместить в
W = 600
H = 400

image = Image.new('RGB',
                  (W, H),
                  (0, 163, 232))

draw = ImageDraw.Draw(image)

text = 'Солнечный день'
# draw.ellipse((470, -120, 800, 120), outline='yellow', fill='yellow')
draw.circle((600, 0), 100, fill='yellow')
font = ImageFont.truetype(
    font='fonts/Geisha.ttf',  # можно использовать любой установленный шрифт, ссылка на скаченный шрифт
    size=50
)
# Получаем размеры текста
_, _, w, h = draw.textbbox((0, 0), text, font=font) # _ означает что переменная не используется

# Рассчитываем позицию для центрирования
x = (W - w) // 2
y = (H - h) // 2

draw.text((x, y), text, fill=(255, 255, 0), font=font)

image.save('images/sunny_day.jpg')
