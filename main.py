# Встроенные библиотеки
# PyPI - Python Package Index (pypi.org)

import random as r

lst = [1,2,3,4,5,6,7,8,9]
res = r.choice(lst)
print(res)

print(r.choice(['орел','решка'])) # случайный выбор (работает со всем кроме словаря и множеств)
#--------------------------------------------------------------
'''import random as r
for _ in range(10):
    #print(r.randint(0,10)) случайные числа от 0 до 10
    print(r.randrange(0,10,2)) # начало с 0, остановка 10 и шаг 2'''



# работа с большим объемом данных choice
