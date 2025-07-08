# Регулярные выражения (поиск по паттерну)
# Regular Expressions
# r - строка -raw-string ("сырая" строка)
'''
import re

pattern = r'\b\w{4}\b'   #все слова из 4х символов  (r'' - регулярное выражение )
test_string = 'дома было холодно'

#<re.Match object; span=(8, 10), match='20'> span где в строке находится совпадение, match - что повторяется
#result = re.search(pattern, test_string)
result = re.findall(pattern, test_string) #если много совпадений

print(result)'''

import re

pattern = r'\d'   #все цифры от 0 до 9    (r'\d{3}' 3и цифры подряд)
test_string = '1 телефон 4 112-2'

result = re.findall(pattern, test_string) #если много совпадений
# Тернарный условный оператор (Ternary If)
print('Цифры  есть') if result else print('Цифр нет') #сначала выводится при выполнении условия а вконце если условие не выполнено