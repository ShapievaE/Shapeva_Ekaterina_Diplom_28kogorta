<img width="1280" alt="Screenshot 2025-04-06 at 23 32 29" src="https://github.com/user-attachments/assets/7fbce852-a1f4-42f1-8eaf-da02b24a31b6" />﻿Задание 1. 
SELECT c.login,
    COUNT(o.id) 
FROM  "Couriers" AS c
LEFT JOIN "Orders" AS o ON o."courierId" = c.id AND o."inDelivery" = true
GROUP BY  c.id;

Задание 2. 
SELECT track,
(CASE WHEN "finished" = true THEN 2 
WHEN "cancelled" = true THEN -1 
WHEN "inDelivery" = true THEN 1 
ELSE 0
END) AS status
FROM "Orders";

Задание 3. 
1. `configuration.py` - содержит данные, такие как URL, которые помогают достучаться до API.
   - `URL_SERVICE` - содержит основное протокол (HTTPS) и доменное имя веб сайта
   - `CREATE_ORDER_PATH` - содержит путь для создания заказа
   - `GET_ORDERS_PATH` - содержит путь для получения заказа по номеру
2. `data.py` — содержит данные, такие как тело данных для заказа:
   - `order_body` — содержат данные для создания заказа
3. `sender_stand_request.py` — файл, содержащий функции для отправки HTTP-запросов:
   - `post_new_body(body)` — отправляет POST-запрос для создания нового заказа.
   - `get_order_by_track` — отправляет GET-запрос для получения заказа по трек-номеру.
4. Правила запуска тестов на проверку параметра name при создании наборов в Яндекс.Прилавок с помощью API Яндекс.Прилавок:
A. Для запуска тестов необходимо установлить библиотеку requests.
B. Для запуска тестов необходимо установлить pytest. Запускать тесты с помощью фреймворка для тестирования- pytest или через команду в терминале.
С. Тесты должны проходить, если возвращаемые коды статусов и данные в ответах соответствуют ожидаемым (например, 201 для успешных запросов и 400 для ошибок).
Примеры тестов:
5. Импортируется тело запроса
6. Выполянется создание заказа (статус - 201)
7. Извлекается трек и проверяется его наличие 
8. По трек выполняется GET-запрос проверяется, что ответ - 200
9. <img width="1280" alt="Screenshot 2025-04-06 at 23 32 29" src="https://github.com/user-attachments/assets/b003312b-7633-48fd-9921-52143e6926d5" />

