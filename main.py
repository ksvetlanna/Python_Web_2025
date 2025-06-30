# Функция enumerate() - в цикле for возвращает пару (i, v)
fio = {'Иванов', 'Петров', 'Сидовор'}
for i, v in enumerate(fio):
    print(f'{i + 1}. {v}') # enumerate нумерует список, можно сразу использовать номер

