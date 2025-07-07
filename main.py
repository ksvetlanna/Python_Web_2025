# Файлы
# name.txt
# t - текстовый файл (txt, html, xml)
# b - бинарные файлы (jpg, avi, mp3)
# w - write (если файла не было то он создается, если файл был то он ПЕРЕЗАПИСЫВАЕТСЯ)
# a - append (запись в конец)
# r - read - чтение (по умолчанию)


fo = open('info.txt', 'at', encoding='utf-8')
#fo.write(' Хороший текст.')
print('\n А вот это будет уже с новой строки.', file=fo)
fo.close()