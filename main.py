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
#------------------------------------------------------------------------------------------
'''раз два три
елочка гори'''
# вывести те слова где в кортеже их меньше и с сортировкой через тире
import sys

data = sys.stdin.readlines()
data = [d.strip('\n') for d in data]

temp = []
# создали пустой список куда сохраним кортежи (номер строки и число строк в строке с этим индексом
for i, s in enumerate(data): # enumerate пронумеровывает список
    temp.append((i, len(s.split()))) # разбиваем строку на слова
temp.sort(key=lambda x:x[1]) # сортируем по 2му элементу (меняем кортежи местами)
#[(1, 2), (0, 3)]
index = temp[0][0]    #
res = sorted(data[index].split()) # разбиваем на слова и выводим через -
print(*res, sep='-')

