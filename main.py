'''a=123456

length=len(str(a))
print(length)'''

word=input('введите слово :')
if not (word) or len(word)<4:
    print('Вы ничего не ввели или слово слишком короткое')
if len(word)>3:
    print('Длина слова "'+ word+'" =', len(word), 'знаков')