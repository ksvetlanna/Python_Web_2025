# Исключения (runtime)

# try:
#   что пытаемся сделать
# except:
#   обрабатываем исключения
#else:
#   если исключения не было
#finally:
#   выполняется в любом случае


## FileNotFoundError: [Errno 2] No such file or directory: 'information.txt' - отсутствует файл
flag = False # открывался ли на запись

try:
    fo = open('information.txt', 'rt', encoding='utf-8')
    print(fo.read())
    fo.close()
except FileNotFoundError: # исключение см. название ошибки выше
    fo = open('information.txt', 'wt', encoding='utf-8')
    flag = True  # если было исключение то проставится flag
    print('Файл не обнаружен и создан по умолчанию')
    '''with open('information.txt','wt', encoding='utf-8') as fo:
        fo.write('По умолчанию')'''

else:
    print('Файл открыт успешно. Читаем его и закрываем.')
    print(fo.read())
    fo.close()
finally:
    if flag: # если файл был открыт на запись (было исключение)
        fo.write('По умолчанию')
        fo.close()
        print('Продолжаем работать.')