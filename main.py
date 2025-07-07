# Пишем и подключаем свои модули
# from . lib import summ - из текущей директории
# from .. lib import summ - из уровня выше
# from .lib import summ - относительный импорт (относительно текущего файла, т.е. в этой же директории  )
from package1 import greet, add, __author__ #* для __all__

print(greet('Мир!'))
print(add(3,7))
print(__author__)
#print(package1.module._hidden_function())