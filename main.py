# удаление
# 1пример
lst = list(range(10))
del lst[2]
print(lst)

# 2пример
lst = list(range(10))
del lst[::2] #удалить каждый 2ой элемент
print(lst)

# 3пример
lst3 = list(range(10))
lst3.pop(5) # удалит значение по индексу 5
print(lst3)


lst4 = [1,7,3,5,4,5,6,4,2]
lst4.sort() # сортирует
print(lst4)