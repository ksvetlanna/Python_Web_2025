# dir - пролистать содержимое каталога
# cd images - попасть в директорию images
# cd .. - выйти на директорию уровнем выше
# mkdir templates - создать папку templates
# rm templates - удалить папку templates (только пустую папку удалит)
# rm -r templates - удалить папку templates (удалит все содержимое папки и потом саму папку)
# con - выводит консоль
# cp info.txt .templates/info.txt - скопировать файл
# mv info.txt .templates/info.txt - переместить файл в другую директорию


import sys
# sys.argv[1] - это аргументы самого скрипта
print('Я', sys.argv[0], 'и мой аргумент', sys.argv[1])  # sys.argv[0] это аргументы скрипта (список)

if len(sys.argv) >= 2:
    match sys.argv[1]:
        case 'p':
            print('Привет')
        case 'g':
            print('Пока')
        case _:
            print('Не понял')

