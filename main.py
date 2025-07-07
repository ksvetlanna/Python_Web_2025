# Файлы
# name.txt
# t - текстовый файл (txt, html, xml)
# b - бинарные файлы (jpg, avi, mp3)
# w - write (если файла не было то он создается, если файл был то он ПЕРЕЗАПИСЫВАЕТСЯ)
# a - append (запись в конец)
# r - read - чтение (по умолчанию)

# построчное чтение №1
'''fo = open('info.txt', 'rt')
while text := fo.readline():
    print(text.rsplit('\n'))
fo.close()'''
#-----------------------------------------------------------------------------------------------------------

# построчное чтение №2
'''fo = open('info.txt', 'rt')
lst = fo.readlines()
lst = list(map(lambda  x: x.strip('\n'), lst))
print(lst)
fo.close()
'''
# построчное чтение №3
#-----------------------------------------------------------------------------------------------------------
fo = open('info.txt', 'rt')
text = fo.read()
lst = text.splitlines()
print(lst)
fo.close()