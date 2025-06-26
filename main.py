# Рост кандидата должен быть от 150 до 180
height = int(input('Введите рост:'))
while not(150 <= height <= 180):
    print(f'Рост кандидата "{height}" не подходит')
    height = int(input('Введите рост:'))
print('Кандидат выбран')