# docker-flaskapi-psql-simple-hh.ru
Simple docker with flask and postgresql hh.ru

### Инструкция:

1. Установить docker и docker-compose.
2. Скачать данный репозиторий.
3. Отредактировать файл docker-compose.yml в блокноте, указать параметры базы данных:
   `POSTGRES_DB: "db" имя базы
   POSTGRES_USER: "postgres" пользователь базы
   POSTGRES_PASSWORD: "123"  пароль базы"`
4.Отредактировать файл __init__.py в блокноте, указать параметры базы данных:
   `app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@postgres/db'
   пример: app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://пользователь:пароль@postgres/имябазы'`
5. Открыть консоль в каталоге репозитория.
6. Выполнить сборку командой docker compose build
7. После успешной сборки запустить сервер командой docker compose up -d
8. Для теста переходим в браузер и переходим http://localhost:5000/sendpost
   Если ответ Post Send то все успешно работает.
9. http://localhost:5000/api/v1/allpost  (получим все записи Вопросов, сортировка от последнего-к первому)
10. Тестовый запрос с аргументами:
   curl -X POST http://localhost:5000/api/v1/post
   -H 'Content-Type: application/json'
   -d '{"questions_num": 10}'
    Где 10 количество получаемых вопросов и возврат последнего из них.
