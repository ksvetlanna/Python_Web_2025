# Области видимости
# Пример как делать НЕЛЬЗЯ!
a =[1,2]

def change_array():
    a[0] = 0
change_array()
print(a)