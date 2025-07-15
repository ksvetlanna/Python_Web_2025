'''
Базы данных (чтение)

1. Импорт библиотеки sqlite3
2. Подключаемся к БД
3. Назначить "курсор"
4. Работа с БД (запросы и ответы)
5. Отключаемся от БД
'''
import sqlite3


connection = sqlite3.connect('db/movies.sqlite')           # Подключение к БД
cursor = connection.cursor()                               # Курсор
result = cursor.execute(                                   # Запрос (с помощью курсора)
    '''
    select title, year from films where year between 2001 and 2005
    '''
)
array = result.fetchall()  # .fetchall() - вывести все строки
                           # .fetchone() - выводит первую запись,
                           # .fetchmany(N) - выводит только то количество строк которое указано в скобках (N)
for title, year in array:
    print(title, year) # вывести на экран результат