from PIL import Image, ImageDraw, ImageFont

orig = Image.open('images/sunny_day.jpg').convert('RGB') # конвертировать в RGB для корректной работы с ним
#               верхняя часть
up = orig.crop((0,0,600,200))
#               нижняя чатсь
down = orig.crop((0,200,600,400))

new = Image.new('RGB', (600,400))

new.paste(down, (0,0))
new.paste(up, (0,200))
new.show()
