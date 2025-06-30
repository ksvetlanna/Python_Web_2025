# 1пример
lst = list(range(10))
for item in lst:
    print(item, '-', item **2)




# 2пример
lst = list(range(10))
slice = lst[1:len(lst):2]
print(slice)
for item in range(0,len(lst),1):
    print(lst[item], '-', lst[item] **2)