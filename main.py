# min, max, average, summ, production
N = 5
total = 0
min_val=float('inf') # +бесконечность
max_val=float('-inf') # +бесконечность
prod=1

for _ in range(N):
    num=int(input('Введите целое число: '))
    if num < min_val:
        min_val=num
    if num > max_val:
        max_val = num
    total += num
    prod *= num
    average = total / N
print(f'Сумма: {total}')
print(f'Произведение: {prod}')
print(f'Ср. арифметическое: {average}')
print(f'Минимум: {min_val}')
print(f'Максимум: {max_val}')