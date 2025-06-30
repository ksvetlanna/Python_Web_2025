# НАЧАЛО И ОКОНЧАНИЕ СТРОКИ
# 1.find('подстрока')
# 2.find('подстрока', start) - с какого места искать (считает от 0)
# 3.find('подстрока', start, end) - с какого места искать и по какое


s = 'синхрофазотрон'
ch='о'


# по умолчанию find ищет первое вхождение, если значение не найдено то выведет -1
'''index = s.find('еть') # с начала строки s
print(index)

index = s.find('еть', 10) # ищет с позиции start
print(index)

index = s.find('ер', 10, 15) # ищет в промежутке с позиции start по end
print(index)'''

if ch in s:
    count=s.count(ch)
    print(f'Буквы {ch} встречается в слове {s} {count} раз.')
    print('Её позиция/позиции:', end=' ')
    start=0
    for i in range(count):
        pos = s.find(ch, start)
        start = pos + 1
        print(pos, end=' ')
else:
    print(f'Буквы {ch} нет в слове "{s}".')


# НАЧАЛО И ОКОНЧАНИЕ СТРОКИ
# 1.replace('что', 'на что') - полная замена
# 1.replace('что', 'на что', 'сколько раз') - число замен

s = '+7-012-345-67-89'

res=s.replace('-',' (', 1)
res=res.replace('-',') ', 1)
print(res)



print(s.replace('-',' (', 1).replace('-',') ', 1))