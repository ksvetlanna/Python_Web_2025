lst = [] # пустой список
while (item := input('Ингредиент:')) !='':
    lst.append(item)

print(f'У нас есть {len(lst)} ингредиентов: ')
lst.sort()

for i in range(len(lst)):
    print(f'\t{i + 1}. {lst[i]}')