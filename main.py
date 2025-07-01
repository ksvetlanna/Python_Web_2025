# Вложенные списки
# такой список нельзя заполнить программно
# 1)способ
a =[
    [1,2,3],
    [4,5,6],
    [7,8,9],
] # вложенные списки
for row in range(3): # 3 в range это кол-во строк
    for col in range(3):
        print(a[row][col])

# 2)способ
# a = [1, 38.6, True, False, 'sfs', (1,2)]
# обход 2-мерного списка (матрицы)
for row in range(len(a)): # 3 в range это кол-во строк
    for col in range(len(a[row])):
        print(a[row][col])
