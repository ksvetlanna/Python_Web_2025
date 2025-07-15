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

class Crud:
    def __init__(self, db_path):
        self._conn = sqlite3.connect(db_path)                      # подключение к БД
        self._cur = self._conn.cursor()

    def create(self,table_name, name, age):
        self._cur.execute(
            f"""
            INSERT INTO {table_name}(name, age)
            VALUES(?, ?)""", (name, int(age))
        )
        self._conn.commit()

    def read(self, table_name):
        res = self._cur.execute(
            f'Select * from {table_name}'
        ).fetchall()
        for num, name, age in res:
            print(num, name, age)

    def update(self,table_name, id_num, name=None, age=None):
        self._cur.execute(
            f'update {table_name} set name="{name}", age={age} where id={id_num}'
        )
        self._conn.commit()

    def delete(self, id_num, table_name):
        self._cur.execute(
            f'Delete from {table_name} where id<=6'
        )
        self._conn.commit()

   # переопределяем метод уничтожения объектов
    def __del__(self):
        self._cur.close()
        self._conn.close()


db = Crud('db/movies.sqlite')
db.delete(2, 'users')
#db.create('users', 'Дмитрий', 18)
#db.update('users', 8, 'Евгений', 19)
db.read('users')