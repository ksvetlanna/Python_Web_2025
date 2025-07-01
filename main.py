# Списочные выражения (list comprehension)
# 1) Вариант
# squares =[]
# for i in range(10):
#     squares.append(i ** 2)
# print(*squares, sep=', ')

# 2) Вариант
# squares = [i ** 2 for i in range(10)] # список квадратов чисел

# список квадратов четных чисел
squares = [i ** 2 for i in range(10) if i % 2 == 0] # список квадратов чисел, но только четные числа
#          1ая    2ая часть          3яя часть

print(*squares, sep=', ')

#  произведение i и j
print([i * j for i in range(3) for j in range(3)])

# для расшифровки формулы выше
# for i in range(3):
#    for i in range(3):
#        print( i * j)