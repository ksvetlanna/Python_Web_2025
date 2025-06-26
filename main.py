num = 3 # число, которое надо угадать
flag = True # флаг, изменияет значение по событию
var=''

print('Я загадал число, угадай!')

while flag:
    var = int(input('Ваше значение:'))
    if var == num:
        print('Ура. Угадал!')
        flag= not flag   # флаг инвертирован
        # аналогично flag=False
    elif var>num:
        print('Число больше загаданного!')
    else:
        print('Число меньше загаданного!')
print('Приходи еще!')