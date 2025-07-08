# ЗАДАНИЕ:
# файл info.txt содержит:
# 8, 2, 4, 6, 3, 5, 9, 7
# 5, 1, 8, 2, 6, 8, 1, 2
# вывести все данные без повторов и отсортированные



# Файлы и OC-модуль
# name.txt
# t - текстовый файл (txt, html, xml)
# b - бинарные файлы (jpg, avi, mp3)
# w - write (запись, создаётся)
# a - append (запись в конец)
# r - read - чтение (по умолчанию)

# читаем файл построчно
'''
#вариант 1
res = []
with open('info.txt', 'rt', encoding='utf-8') as fo: # файл автоматически закроется когда перейдет на 20 строку
    while temp := fo.readline():
        res += temp.split(', ')

res = list(map(lambda  x: x.rstrip('\n'), res))  # убрали ненужные символы
res = set(res) # убираем все повторы
res = sorted(int(x) for x in res)
print(res)'''
#----------------------------------------------------------------------------------------------------------------
#вариант 2
res = []
with open('info.txt', 'rt') as f:
    while temp := f.readline().rstrip('\n'): #readline-читаем строку до пустой строки
        res += temp.split(', ')

res = sorted(int(x) for x in set(res))
print(res)