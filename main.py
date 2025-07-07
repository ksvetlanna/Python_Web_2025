# Файлы
# name.txt
# t - текстовый файл (txt, html, xml)
# b - бинарные файлы (jpg, avi, mp3)
# w - write (если файла не было то он создается, если файл был то он ПЕРЕЗАПИСЫВАЕТСЯ)
# a - append (запись в конец)
# r - read - чтение

fo  = open('info.txt', 'wt', encoding='utf-8') # fo -файл (если 2ой параметр отсутствует то мы планируем открыть на чтение)
print(fo.mode) # режим
print(fo.name) #имя файла
print(fo.encoding) # кодировка
count = fo.write('Этот текст будет в файле!')
print('В файле записано', count, 'байт')

fo.close()