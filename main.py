# Встроенные библиотеки
# datetime работает с датой  и временем
'''import datetime as dt

print(dt.datetime.now())
print(dt.datetime.now().date())
print(dt.datetime.now().time())

time = dt.datetime.now()

fdat = time.strftime('%d/%m/%y') # маска для вывода d-день m-месяц y-год

print('Сегодня: ', fdat)

ftime = time.strftime('%H:%M:%S') # маска для вывода H-часы M-минуты S-секунды

print('Время: ', ftime)'''
#----------------------------------------------------------------------------

import datetime as dt
my_time = dt.time(15,27,32)
print(my_time) #выводит объект который потом нужно преобразовать в строку
my_dat = dt.date(2025,7,4)
print(my_dat)

my_dat_time = dt.datetime.combine(my_dat, my_time) # combine - соединяет (комбинирует)
print(my_dat_time)

date1 = dt.date(2025,6,15)
date2 = dt.date(2025,7,3)
dalta = date2-date1

print(dalta)
#----------------------------------------------------------------------------