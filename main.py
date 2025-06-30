# удаление
# 1пример
a = ['a','b','c']
b = a.copy()   # или  a[:] полный срез от а записать в b
b.append('d')
print(id(a))
print(id(b))
print(a)
print(b)