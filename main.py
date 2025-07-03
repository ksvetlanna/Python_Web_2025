# проверка коллекций: any(), all()
# any - любой элемент коллекции вернул True
# all - все элементы коллекции вернули True
import sys

print(all([1,2,3])) # все элементы не нулевые

print(all([1,2,0])) # один элемент нулевой

print(all([]))

words = 'один два три'.split() # >3
#list_for_analize = list(map(lambda x: len(x) > 3, words))
print(all(list(map(lambda x: len(x) > 3, words))))

#------------------------------------------------------------------------------------------
# потоковый ввод sys.stdin (Ctrl + D)
'''import sys

for line in sys.stdin:
    print(line)'''


import sys

data = sys.stdin.readlines()
data = [d.strip('\n') for d in data]
print(data)