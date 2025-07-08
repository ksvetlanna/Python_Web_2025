# Утверждения (assertions)
# В основном для нужд тестирования
try:
    text = input('Введите текст: ')
    assert len(text) > 3 # это утверждение
except AssertionError:
    print('Слишком короткий текст')