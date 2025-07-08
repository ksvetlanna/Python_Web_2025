# Регулярные выражения (поиск по паттерну)
# Regular Expressions
# Квантификаторы (quantity)
# r - строка -raw-string ("сырая" строка)
# {m} -ровно m раз
# {m,} -ровно m раз и более
# {,n} - не более n раз
# {m,n} - от m до n (без пробела)
# ? - от 0 до 1 (аналог {0,1})
# * - от 0 до бесконечности (32767) {,0}
# + - от 1 до беконечности (32767) {1,}
'''
import re

#pattern = r'начало!\Z    # на что заканчивается
#pattern = r'[0-5][0-9]'   #2числа идут подряд и изменяются от 0-5 и 0-9
#pattern = r'[а-яА-Я]' #все буквы от а до я и от А до Я
#pattern = r'\((.+?)\)' вытащить текст из скобок
pattern = '[^ерм]' # исключение символов указанных в кавычках
test_string = 'Время - 07:55'

result = re.findall(pattern, test_string) # если много совпадений

print(result)'''
'''
import re

pattern = r'\((.+?)\)'
test_string = 'Поиск по образцу (pattern)'

result = re.findall(pattern, test_string) # если много совпадений
print(result)'''

import re

pattern = 'Go{2,}gle'
test_string = 'Google, Goooogle, Goooooooogle'
result = re.findall(pattern, test_string)
print(result)