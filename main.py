# CSV-файлы

import csv

data = [
    ['name', 'age', 'city'],
    ['Борис', '25', 'Воронеж'],
    ['Александр', '39', 'Омск'],
    ['Павел', '48', 'Москва']
]

with open('people.csv','r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        print(row)

with  open('employee.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data) # убираем лишние отступы в виде пустых строк
