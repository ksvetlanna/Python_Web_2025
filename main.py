# Функция sorted()
s = {'Иванов', 'Петров', 'Сидовор'} # множество
r = True # False
lst = sorted(s, reverse=r)
#lst = sorted(s) 1ый способ
#lst = list(s) 2ой способ тоже самое что и сточка выше
#lst.sort() 2ой способ тоже самое что и сточка выше
print(*lst, sep=', ')