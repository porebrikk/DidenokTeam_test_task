# Тестовое задание Didenok Team
Менеджер паролей.
Пароли хранятся в бд в зашифрованном виде, с привязкой к имени сервиса, который указывается при создании пароля.
Шифрование реализовано с помощью <a href="https://github.com/kvesteri/sqlalchemy-utils">sqlalchemy-utils</a> и <a href="https://github.com/pyca/cryptography">cryptography</a>.

Используемый стэк:
1. <a href="https://www.python.org/downloads/release/python-3110/">Python 3.11</a>
2. <a href="https://github.com/pallets/flask/">Flask</a> / <a href="https://github.com/python-restx/flask-restx">Flask-RESTX</a>
3. <a href="https://github.com/sqlalchemy/sqlalchemy">SQLAlchemy</a> / <a href="https://github.com/python/cpython/blob/main/Doc/library/sqlite3.rst">SQLite3</a>
4. <a href="https://github.com/docker">Docker</a>
5. <a href="https://github.com/pytest-dev/pytest/">Pytest</a>

Порядок запуска:
1. Сделать клон репозитория:
```
git clone https://github.com/porebrikk/didenok_team.git)
```
3. Перейти в папку **didenok_team**;
4. Запустить контейнеры с базой данных и приложением:
```
docker-compose up -d --build
```
6. Для работы с API использовать адрес:
```
http://127.0.0.1:5000/
```
7. Доступные эндпоинты:

GET:
   > Получение пароля по полному наименованию сервиса:
```
http://127.0.0.1:5000/password/<наименование сервиса>
```
  > Формат ожидаемого ответа:
```
{
  "service_name": "string",
  "password": "string"
}
```
  > Получение пароля по части наименования сервиса:
```
http://127.0.0.1:5000/password/?service_name=<наименование сервиса>
```
  > Формат ожидаемого ответа:
```
{
  "service_name": "string",
  "password": "string"
}
```
  POST:
  > Создание пароля с указанием наименования сервиса:
```
http://127.0.0.1:5000/password/<наименование сервиса>
```
```
{
  "password": "string"
}
```
  > Формат ожидаемого ответа:
```
{
  "password": "string"
}
```
