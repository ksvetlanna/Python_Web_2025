hour=int(input('введите время от 0 до 23 :'))
if hour>23:
    hour=23
if hour<0:
    hour = 0
if 7 <= hour <= 11:
    print('Доброе утро')
    if 12 <= hour <= 17:
        print('Добрый день')
    if 18 <= hour <= 22:
        print('Доброе вечер')
else:
    print('Доброй ночи')