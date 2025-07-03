# Анонимные функции (однострочники, безымянные)
# lambda - функции
# lambda <аргументы>: <выражение>
# словарные выражения

# создать словарь четных чисел от 1 до 10
range(2,10)
squares = {n: n**2 for n in range(2,10) if n%2 ==0}
print(squares)

source_dict = {
    'x': 1,
    'y': 2,
    'z': 3,
}
dest_dict = {k: v * 2 for k, v in source_dict.items()}
print(dest_dict)

