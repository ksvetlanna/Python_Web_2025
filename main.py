# Пишем и подключаем свои модули
# from . lib import summ - из текущей директории
# from .. lib import summ - из уровня выше
# from .lib import summ - относительный импорт (относительно текущего файла, т.е. в этой же директории  )
'''import lib
lib.diff()

или'''

from lib import summ


def main():
    print(summ(7, 3))

# __name__ возвращает имя всего к чему обращаемся
if __name__ == '__name__':
    main()