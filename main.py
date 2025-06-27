'''phrase=('Язык Python')

print(phrase.lower()) #все буквы маленькие
print(phrase.upper()) #все буквы большие
print(phrase.capitalize()) #только первая буква заглавная
print(phrase.title()) #все слова с заглавной буквы

print('Ура! '*3) #размножит фразу столько раз на сколько умножим
print('Телевизор'.count('е')) # посчитать сколько раз буква е присутствует в слове Телевизор
print('Python'.index('h')) #по символу h определяем какую позицию (index)'''


'''word = 'статор'
res = ''
for ch in word:
    i = word.index(ch)+1
    print(ch*i, end='')'''

word = 'статор'
res = ''
for i in range(1,len(word)+1):
    print(word[i-1]*i, end='')