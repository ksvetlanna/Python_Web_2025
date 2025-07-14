# CSV-файлы (strptime) строку переводит в двату

import csv

# режим кватирования (QUOTE_NONNUMERIC)
data = ['name', 25, 'town']
with open('sample.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC) #записать все в '' но числа в кавычки не заключать
    writer.writerow(data)