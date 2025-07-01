# Списочные выражения (list comprehension)
n = '500 600 700 800'
# a = [int(i) for i in n.split()] так же можно присвоить в переменную для дальнейшей работы
print([int(i) for i in n.split()])



n = '100 200 300 400 500 600 700 800 900'
approved = [500, 800]
a = [int(i) for i in n.split() if int(i) in approved]
print(a)