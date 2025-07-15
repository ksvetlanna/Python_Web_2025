'''
Базы данных (измепнения)

1. Импорт библиотеки sqlite3
2. Подключаемся к БД
3. Назначить "курсор"
4. Работа с БД (запросы и ответы)
5. Подтвердить изменения
6. Отключаемся от БД

CREATE TABLE users (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,                        # уникальный ключ, будет автоматом добавлять 1
    name TEXT    NOT NULL,
    age  INTEGER NOT NULL
);

insert into                                                        # добавление записей в таблицу
users(name, age)
values('Molly',14),
('Julia',25)

update users set age=22
where id=2                                                         # обновить данные в таблице

delete from users where age > 30                                   # удалить
'''

import sqlite3
import csv


with open('people.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader) #пропустить первую строку (заголовок кот. есть в фале)

    connection = sqlite3.connect('db/movies.sqlite')           # Подключение к БД
    cursor = connection.cursor()                               # Курсор
    for name, age in reader:
        cursor.execute(
        '''
        insert into users(name, age)
        values(?, ?)
        ''', (name , int(age))                       # заголовок который использовался в файле
    )
connection.commit()
connection.close()                                         # отключаемся от БД