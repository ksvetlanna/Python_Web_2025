'''
from PIL import Image, ImageFilter, ImageEnhance

orig = Image.open('images/Python.jpg').convert('RGB')

blur_image = orig.filter(ImageFilter.GaussianBlur(radius=2)) # размытие, можно делать больше или меньше
blur_image.show()'''
#-----------------------------------------------------------------------------------------------------
'''from PIL import Image, ImageFilter, ImageEnhance

orig = Image.open('images/Python.jpg').convert('RGB')
# усиление резкости
enchancer = ImageEnhance.Sharpness(orig)
sharpened_image = enchancer.enhance(4.0) # четкость
sharpened_image.show()'''
#-----------------------------------------------------------------------------------------------------
#контуры
from PIL import Image, ImageFilter, ImageEnhance

orig = Image.open('images/Python.jpg').convert('RGB')
# Получить контуры
edges = orig.filter(ImageFilter.FIND_EDGES)

edges.show()