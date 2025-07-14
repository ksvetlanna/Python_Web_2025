import json

with open('dogs.json', 'rt') as d:
    # data = json.load(d) # Напрямую из файла
    temp = d.read()  # читаем файл как строку
    data = json.loads(temp)  # строковое представление JSON

for i in range(len(data)):
    print(f'Питомец №{i + 1}:')
    for k, v in data[i].items():
        if type(v) == list:
            print(f'\t{k}: {', '.join(v)}')
        else:
            print(f'\t{k}: {v}')