# цветовая схема (что бы узнать цвет) или посмотреть в paint
from PIL import Image, ImageDraw # базовые манипуляции с изображением

image = Image.new('RGB',
                  (600, 400),
                  (0, 0, 255)) # создаем объект
RED = (255, 0, 0)
POLY = [(50,50),(150,50), (180,120)]
draw = ImageDraw.Draw(image)
draw.line((0, 0, 600, 400), fill=RED, width=5)
draw.line((600, 0, 0, 400), fill=RED, width=5) # перечеркнутая линия с другой стороны
draw.rectangle((10, 10, 590, 390), outline=RED, width=10)
draw.ellipse((10, 10, 590, 390), outline=RED, width=10)

draw.polygon(POLY, outline='green', width=15)
draw.text((100, 100), 'Hello!', font_size=25, fill=RED)
image.save('images/blue.jpg')