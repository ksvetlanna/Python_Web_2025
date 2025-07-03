# Анонимные функции (однострочники, безымянные)
# lambda - функции
# lambda <аргументы>: <выражение>

# сформировать список английского алфавита
english_abc = set([chr(ch) for ch in range(ord('a'), ord('z') +1)])
#print(english_abc)
#----------------------------------------------------------------------------------------------------

# сформировать список русского алфавита
russian_abc = set([chr(ch) for ch in range(ord('а'), ord('я') +1)]+['ё'])
#print(russian_abc)

# ^ только уникальные элементы множеств english_abc и russian_abc
ABC = english_abc ^ russian_abc
print(ABC)

text = 'Однажды, теперерь.'.lower()
text = ''. join(filter(lambda x: x in ABC ^ {' '}, text))
print(text)