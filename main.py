# https://regex101.com сайт с регулярными выражениями
# Регулярные выражения (поиск по паттерну)
# Regular Expressions
# Квантификаторы (quantity)
# r - строка -raw-string ("сырая" строка)
# {m} -ровно m раз
# {m,} -ровно m раз и более
# {,n} - не более n раз
# {m,n} - от m до n (без пробела)
# . - абсолютно любой символ
# ? - от 0 до 1 (аналог {0,1})
# * - от 0 до бесконечности (32767) {,0}
# + - от 1 до бесконечности (32767) {1,}
#pattern = r'начало!\Z    # на что заканчивается
#pattern = r'[0-5][0-9]'   #2числа идут подряд и изменяются от 0-5 и 0-9
#pattern = r'[а-яА-Я]' #все буквы от а до я и от А до Я
#pattern = r'\((.+?)\)' вытащить текст из скобок "\(" и "\)" символы экранирования
#pattern = '[^ерм]' # исключение символов указанных в кавычках
#pattern = r'стеклянн?ый' #2-я может присутствовать
#pattern = r'<img.*>' #"жадный" квантификатор
#pattern = r'<img.*?>' # ленивый квантификатор
#pattern =  r'<img[^>]+src="([^">]+)"' # только путь к картинке
#pattern =  '<p>(.*?)</p>'   # вытащить только текст из html документа
#pip install requests
#pip freeze > requirements.txt


import re
import requests

# сначала проверили
pattern = r'<img[^>]+src="([^">]+)"'
html = requests.get('https://skillbox.ru').text
#test_string = '<>img height="50" width="150" src="image/bg.jpg"'
result = re.findall(pattern, html)
print(result)

#print(html)
#вернулся объект
#<Response [200]>