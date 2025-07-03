#варианты сортировки
#сортировка по длинне словаа
#fruits = ['арбуз', 'ананас', 'банан', 'ежевика', 'малина']
# print(sorted(fruits, key=lambda ch: len(ch)))


ENGLISH_ABC = [chr(ch) for ch in range(ord('a'), ord('z') + 1)]
RUSSIAN_ABC = [chr(ch) for ch in range(ord('а'), ord('я') + 1)] + ['ё']
ABC = (set(ENGLISH_ABC) ^ set(RUSSIAN_ABC) ^
       set([x.upper() for x in ENGLISH_ABC]) ^
       set([x.upper() for x in RUSSIAN_ABC]))
# print(ABC)
# print(ENGLISH_ABC)
# print(RUSSIAN_ABC)
txt = 'Я знаю, что я ничего не знаю. Но другие не знают и этого. А значит, я знаю больше, чем они.'

d={}


def remove_punctuation(text):
    return ''.join(filter(lambda x: x in ABC ^ {' '}, text))


def get_words(text: str) -> list:
    return remove_punctuation(text).split()


def long_words(text, length=4) -> filter:
    return filter(lambda word: len(word) >= length, get_words(text))


words = get_words(txt.lower())
print(words)

# считаем частоту слов
for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

# reverse сортировать по количеству
res = {k: v for k,v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

for k,v in d.items():
   print(k, v)

# ключ сортировки
