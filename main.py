# CSV-файлы

import csv

from urllib3.filepost import writer

with open('people.csv','r', encoding='utf-8') as f:
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        print(f'{row['name']} живет в городе {row['city']}')

field_name=['name','age','city']

data = {
    'name' : 'Борис',
    'age' : '25',
    'city' : 'Воронеж'
}

with open('file.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=field_name)
    writer.writerow(data)