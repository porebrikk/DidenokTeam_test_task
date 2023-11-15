# DidenokTeam_test_task
Менеджер паролей.
Пароли хранятся в бд в зашифрованном виде, с привязкой к имени сервиса, который указывается при создании пароля.

Порядок запуска:
1. Сделать клон репозитория (git clone https://github.com/porebrikk/didenok_team.git);
2. Перейти в папку didenok_team;
3. Запустить базу данных и приложение с помощью команды docker-compose up.
(в случае ошибки типа "Could not locate a Flask application" рекомендуется выполнить команду docker compose up --build -d).
