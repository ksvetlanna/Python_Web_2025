# JSON - Java Script Object Notation
# Для чтения :
# load() - читает из файл
# loads() - читает строковое представление

import json


with open('dogs.json','rt') as d:
   # data = json.load(d) #напрямую из файла
   temp=d.read() # читаем как строку
   data = json.loads(temp) # строковое представление JSON

for k, v in data.items():
    if type(v) == list:
        print(f'{k}: {', '.join(v)}')
    else:
        print(f'{k}: {v}')