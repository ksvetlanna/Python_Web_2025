# Вложенные списки
# Задание: заполнить список программно
# 1) вариант
N = 3
matrix=[[1]*N for _ in range(N)] # вместо 1 можно указать любое число
print(matrix)

count = 1
for row in range(len(matrix)): # 3 в range это кол-во строкAdd commentMore actions
    for col in range(len(matrix[row])):
        matrix[row][col] = count
        count +=1
print(matrix)


# 2) вариант
matrix = []
start = 1
N = 4

for i in range(N):
    table = []
    for j in range(start, start + N):
        table.append(j)
    matrix.append(list(table))
    start += N
print(matrix)

# 3) вариант
matrix=[[i+j for j in range(N)] for i in range(1,10,3)]
print(matrix)