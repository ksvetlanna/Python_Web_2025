# Функция, как объект
# Передаётся в другие функции: функции высшего порядка

# Функция критерия отбора элементов списка
# Критерий: длина слова
def is_longer_six(word):
    return len(word) > 6


# Критерий - первая буква
def is_first_letter_a(word):
    return word[0] == 'а'


def square(num):
    return num ** 2


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9] # 123456789
squares = map(square, nums)
print(list(squares))



words = ['В', 'этом', 'списке', 'останутся', 'слова',
         'длина', 'которых', 'больше', 'шести']

fruits = ['арбуз', 'ананас', 'банан', 'ежевика', 'малина']

result = list(filter(is_longer_six, words))
print(result)

res = list(filter(is_first_letter_a, fruits))
print(res)

for word in filter(is_longer_six, words):
    print(word)