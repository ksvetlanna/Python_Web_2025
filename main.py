# Анонимные функции (однострочники, безымянные)
# lambda - функции
# lambda <аргументы>: <выражение>

# сформировать список английского алфавита
english_abc = set([chr(ch) for ch in range(ord('a'), ord('z') +1)])
russian_abc = set([chr(ch) for ch in range(ord('а'), ord('я') +1)]+['ё'])

# ^ только уникальные элементы множеств english_abc и russian_abc
ABC = english_abc ^ russian_abc

txt = 'Однажды, теперь и потом.'.lower()
# очищает текст от лишних символов таких как (, - :)
def remove_punctuation(text):
    return ''. join(filter(lambda x: x in ABC ^ {' '}, text))



def get_words(text: str) -> list:
    return remove_punctuation(text).split()


# возвращает список слов длинна которых больше или равна 4
def long_words(text, length=4) -> filter:
    return filter(lambda word: len(word) >= length, get_words(text))


print(list(long_words(txt)))