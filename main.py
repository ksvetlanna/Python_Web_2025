# Рекурсия - функция вызывает сама себя
'''def factorial(count): # если факториал 5 = 1 * 2 * 3 * 4 * 5 = 120
    result = 1
    for i in range(2, count +1):
        result *= i
    return result

for x in range(10):
    print(x, factorial(x))'''

#-------------------------------------------------------------------------------------
#функция вызывает сама себя и первое, что прописываем это условие выхода из функции
def factorial(x):
    if x == 1 or x == 0:      # базовый вариант
        return 1
    return x * factorial(x-1) # рекурсивная пружина


for x in range(10):
    print(x, factorial(x))