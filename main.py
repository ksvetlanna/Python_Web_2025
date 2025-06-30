# Списки (list)
# lst =[] пустой список
#1 пример
s='Собака'
lst =list(s)
lst[1] = 'о'
print(lst)

#2 пример
f= []
for i in range(11):
    f.append(i)
print(f)

#3 пример
s1 = [1,2,3]
s2 = [4,5,6]
ss = s1 + s2  # с помощью + можно канкатинировать и списки
print(ss)