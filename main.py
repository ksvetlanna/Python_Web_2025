# Города
s = set()

while (city := input('Назовите город: ')) != '':
    if city in s:
        print('Такой город уже был')
    else:
        s.add(city)
print(f'Итого было названо: {len(s)} городов: ')
for item in s:
    print('\t', item)