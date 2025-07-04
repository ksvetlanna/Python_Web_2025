# Встроенные библиотеки
# PyPI - Python Package Index (pypi.org)
# сгенерировать НЕ ПОВТОРЯЮЩИЕСЯ значения из списка
'''
import random as r
lst = [1,2,3,4,5,6,7,8,9]

for _ in range(10):
    print(r.sample(lst, k=5))
'''
#-----------------------------------------------------------------------------------
'''import random as r

abc = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
lst = list(abc)
r.shuffle(list(lst))
print(lst)'''
#-----------------------------------------------------------------------------------
#генерация случайного пароля, 8и значный, 1-ин символ,
import random as r

N = 8
abc = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
num = '123456789'
spec ='@#$%&*~`'

abc =list(abc)
num =list(num)
spec =list(spec)

r.shuffle(abc)

temp = abc[:N - 3]
temp.append(r.choice(abc).upper())
temp.append(r.choice(num))
temp.append(r.choice(spec)) # choice перетосовать значения
r.shuffle(temp) # shuffle выбрать случайное значение
res = ''.join(temp)

print(res)