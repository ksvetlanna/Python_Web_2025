#задача посчитать сколько человек пришло, выбрать сколько подходит по росту от 150 до 180 и макс и мин определить
total = 0
total_success = 0
total_unsuccess = 0
min_val = float('inf')
max_val = float('-inf')

while (num := int(input('Введите рост:'))) !=-1:
    if 150 <= num <= 180:
        total_success += 1
        if min_val > num:
            min_val=num
        if num > max_val :
            max_val = num
    total +=1
print(f'Число кандидатов: {total}')
print(f'Число прошедших отбор: {total}')
print(f'Минимальный рост: {min_val}')
print(f'Максимальный рост: {max_val}')