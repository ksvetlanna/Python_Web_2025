
import json


d = {
    'ананас': 300,
    'банан': 400,
    'яблоко': 120,
    'груша': 280,
}
#запись напрямую в файл
#with open('fruits.json', 'w', encoding='utf-8') as f:
#    json.dump(d, f, indent=4)

#вывод в виде строки без сохранения в файл
date = json.dumps(d, indent=4)
print(date)