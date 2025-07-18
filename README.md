### Обновленные скрипты с полем `photo` в таблице `apartments`

#### 1. Создание таблиц и индексов (с полем photo)
```sql
-- Удаление существующих таблиц
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS rentals;
DROP TABLE IF EXISTS tenants;
DROP TABLE IF EXISTS apartments;
DROP TABLE IF EXISTS owners;

-- Создание таблиц
CREATE TABLE owners (
    owner_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE apartments (
    apartment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_id INTEGER NOT NULL,
    address TEXT NOT NULL,
    rooms INTEGER NOT NULL CHECK (rooms > 3),
    area REAL NOT NULL CHECK (area > 0),
    photo TEXT CHECK(photo IS NULL OR 
                    photo LIKE '%.jpg' OR 
                    photo LIKE '%.jpeg' OR 
                    photo LIKE '%.png' OR 
                    photo LIKE '%.gif' OR 
                    photo LIKE '%.tiff'), -- Разрешенные форматы
    description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (owner_id) REFERENCES owners(owner_id) ON DELETE CASCADE
);

CREATE TABLE tenants (
    tenant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    passport TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE rentals (
    rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
    apartment_id INTEGER NOT NULL,
    tenant_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL CHECK (end_date > start_date),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (apartment_id) REFERENCES apartments(apartment_id) ON DELETE CASCADE,
    FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id) ON DELETE CASCADE
);

CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    apartment_id INTEGER NOT NULL,
    tenant_id INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (apartment_id) REFERENCES apartments(apartment_id) ON DELETE CASCADE,
    FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id) ON DELETE CASCADE,
    FOREIGN KEY (owner_id) REFERENCES owners(owner_id) ON DELETE CASCADE
);

-- Создание индексов
CREATE INDEX idx_apartments_owner ON apartments(owner_id);
CREATE INDEX idx_rentals_apartment ON rentals(apartment_id);
CREATE INDEX idx_rentals_tenant ON rentals(tenant_id);
CREATE INDEX idx_reviews_tenant ON reviews(tenant_id);
CREATE INDEX idx_reviews_apartment ON reviews(apartment_id);
CREATE INDEX idx_tenants_passport ON tenants(passport);
```

#### 2. Заполнение таблиц тестовыми данными (с фото)
```sql
-- Владельцы (10 записей)
INSERT INTO owners (full_name, phone, email) VALUES
('Иванов Петр Сергеевич', '+79161234501', 'ivanov@example.com'),
('Смирнова Ольга Владимировна', '+79161234502', 'smirnova@example.com'),
('Кузнецов Андрей Игоревич', '+79161234503', 'kuznetsov@example.com'),
('Попова Екатерина Дмитриевна', '+79161234504', 'popova@example.com'),
('Васильев Михаил Александрович', '+79161234505', 'vasilev@example.com'),
('Новикова Анна Сергеевна', '+79161234506', 'novikova@example.com'),
('Федоров Денис Олегович', '+79161234507', 'fedorov@example.com'),
('Морозова Татьяна Викторовна', '+79161234508', 'morozova@example.com'),
('Лебедев Артем Николаевич', '+79161234509', 'lebedev@example.com'),
('Соколова Ирина Павловна', '+79161234510', 'sokolova@example.com');

-- Квартиры (15 записей с фото)
INSERT INTO apartments (owner_id, address, rooms, area, photo, description) VALUES
(1, 'ул. Тверская, д. 10, кв. 25', 4, 85.5, 'kremlin_view.jpg', 'Просторная квартира с видом на Кремль'),
(2, 'пр. Ленина, д. 15, кв. 42', 5, 110.0, 'euro_remont.png', 'Евроремонт, панорамные окна'),
(3, 'ул. Пушкина, д. 7, кв. 13', 4, 92.3, 'park_view.jpeg', 'Рядом с парком, тихий двор'),
(1, 'ул. Гагарина, д. 33, кв. 18', 6, 145.0, 'penthouse_terrace.tiff', 'Пентхаус с террасой'),
(4, 'пр. Мира, д. 22, кв. 7', 4, 88.7, 'modern_design.jpg', 'Современный дизайн интерьера'),
(5, 'ул. Лермонтова, д. 12, кв. 31', 5, 105.5, 'fireplace_living.png', 'Камин, высокие потолки'),
(6, 'наб. Невы, д. 5, кв. 9', 7, 180.0, 'river_view.jpeg', 'Вид на реку, 2 балкона'),
(7, 'ул. Чехова, д. 8, кв. 21', 4, 86.0, NULL, 'С мебелью и техникой'),  -- Без фото
(8, 'пр. Победы, д. 17, кв. 34', 5, 112.3, 'premium_remont.jpg', 'Ремонт премиум-класса'),
(9, 'ул. Горького, д. 3, кв. 11', 4, 90.5, 'kitchen_living.gif', 'Кухня-гостиная 40 кв.м'),
(10, 'ул. Садовая, д. 20, кв. 5', 6, 138.0, 'luxury_bathrooms.png', '3 санузла, гардеробная'),
(2, 'ул. Цветочная, д. 14, кв. 27', 4, 87.5, 'heated_floors.jpg', 'Теплые полы, кондиционер'),
(3, 'пр. Космонавтов, д. 9, кв. 16', 5, 107.8, NULL, 'Лоджия 10 кв.м'),  -- Без фото
(4, 'ул. Лесная, д. 1, кв. 33', 4, 91.2, 'home_office.jpeg', 'Кабинет, детская комната'),
(5, 'ул. Маяковского, д. 25, кв. 8', 5, 115.0, 'smart_home.tiff', 'Система "умный дом"');

-- Арендаторы (15 записей)
INSERT INTO tenants (full_name, passport, phone) VALUES
('Петров Алексей Иванович', '4510123456', '+79162345601'),
('Сидорова Марина Викторовна', '4511123456', '+79162345602'),
('Николаев Денис Петрович', '4512123456', '+79162345603'),
('Козлова Анастасия Олеговна', '4513123456', '+79162345604'),
('Орлов Игорь Сергеевич', '4514123456', '+79162345605'),
('Андреева Елена Дмитриевна', '4515123456', '+79162345606'),
('Тарасов Павел Андреевич', '4516123456', '+79162345607'),
('Филиппова Ольга Игоревна', '4517123456', '+79162345608'),
('Белов Артем Владимирович', '4518123456', '+79162345609'),
('Григорьева Татьяна Николаевна', '4519123456', '+79162345610'),
('Данилов Максим Александрович', '4520123456', '+79162345611'),
('Киселева Юлия Вадимовна', '4521123456', '+79162345612'),
('Семенов Виктор Олегович', '4522123456', '+79162345613'),
('Мельникова Ирина Сергеевна', '4523123456', '+79162345614'),
('Волков Дмитрий Алексеевич', '4524123456', '+79162345615');

-- Аренды (15 записей)
INSERT INTO rentals (apartment_id, tenant_id, start_date, end_date) VALUES
(1, 1, '2023-01-15', '2023-12-31'),
(2, 2, '2023-02-01', '2024-01-31'),
(3, 3, '2023-03-10', '2023-09-30'),
(4, 4, '2023-04-05', '2024-04-05'),
(5, 5, '2023-05-20', '2023-11-20'),
(6, 6, '2023-06-01', '2024-05-31'),
(7, 7, '2023-07-15', '2024-07-14'),
(8, 8, '2023-08-01', '2024-02-01'),
(9, 9, '2023-09-10', '2024-03-10'),
(10, 10, '2023-10-05', '2024-04-05'),
(11, 11, '2023-11-01', '2024-05-31'),
(12, 12, '2023-12-10', '2024-06-10'),
(13, 13, '2024-01-15', '2024-07-15'),
(14, 14, '2024-02-01', '2024-08-01'),
(15, 15, '2024-03-10', '2024-09-10');

-- Отзывы (10 записей)
INSERT INTO reviews (apartment_id, tenant_id, owner_id, rating, comment) VALUES
(1, 1, 1, 5, 'Отличная квартира, прекрасный вид! Хозяин очень отзывчивый'),
(2, 2, 2, 4, 'Удобное расположение, но шумно по вечерам'),
(3, 3, 3, 5, 'Идеальное соотношение цена/качество. Рекомендую!'),
(4, 4, 1, 3, 'Пентхаус хорош, но отопление зимой слабое'),
(5, 5, 4, 5, 'Современный ремонт, все продумано до мелочей'),
(6, 6, 5, 4, 'Уютно, но кухня маленьковата для большой семьи'),
(7, 7, 6, 5, 'Виды Невы стоят каждой копейки! Незабываемо'),
(8, 8, 7, 2, 'Старая мебель, сантехника требует замены'),
(9, 9, 8, 5, 'Премиум-ремонт оправдал ожидания. Все супер!'),
(10, 10, 9, 4, 'Хорошая кухня-гостиная, но слабый интернет');
```

### Особенности реализации поля `photo`:
1. **Тип данных**: `TEXT` для хранения путей к файлам или URL
2. **Проверка форматов**: `CHECK`-ограничение разрешает только:
   - JPEG/JPG (`%.jpg`, `%.jpeg`)
   - PNG (`%.png`)
   - GIF (`%.gif`)
   - TIFF (`%.tiff`)
3. **Необязательное заполнение**: Может быть `NULL`
4. **Примеры значений**:
   - `'kremlin_view.jpg'`
   - `'penthouse_terrace.tiff'`
   - `NULL` (для записей без фото)

### Проверочный запрос:
```sql
-- Просмотр квартир с фото
SELECT apartment_id, address, photo 
FROM apartments 
WHERE photo IS NOT NULL;

-- Просмотр всех квартир (с указанием наличия фото)
SELECT 
    apartment_id,
    address,
    CASE 
        WHEN photo IS NULL THEN 'Нет фото'
        ELSE 'Есть фото: ' || photo
    END AS photo_status
FROM apartments;
```

Эта реализация позволяет:
1. Хранить ссылки на изображения в поддерживаемых форматах
2. Гарантировать корректность форматов через CHECK-ограничение
3. Иметь записи без привязки к фото (NULL значения)
4. Легко интегрироваться с файловой системой или CDN
5. Сохранять нормализованную структуру базы данных
