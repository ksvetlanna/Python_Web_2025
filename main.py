# Файлы
# name.txt
# t - текстовый файл (txt, html, xml)
# b - бинарные файлы (jpg, avi, mp3)
# w - write (если файла не было то он создается, если файл был то он ПЕРЕЗАПИСЫВАЕТСЯ)
# a - append (запись в конец)
# r - read - чтение (по умолчанию)

# Открытие с менеджером контеста
with open('info.txt', 'rt') as fo:
    text = fo.read()
    lst = text.splitlines()
    print(lst)
