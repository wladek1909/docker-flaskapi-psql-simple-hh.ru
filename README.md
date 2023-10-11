# docker-flaskapi-psql-simple-hh.ru
Simple docker with flask and postgresql hh.ru

### Инструкция:

1. Установить docker и docker-compose
2. Скачать данный репозиторий, открыть консоль в каталоге репозитория.
3. Отредактировать файл docker-compose.yml в блокноте, указать параметры базы данных:
   `POSTGRES_DB: "db" имя базы
   POSTGRES_USER: "postgres" пользователь базы
   POSTGRES_PASSWORD: "123"  пароль базы"`
4.Отредактировать файл __init__.py в блокноте, указать параметры базы данных:
   `app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@postgres/db'
   пример: app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://пользователь:пароль@postgres/имябазы'`
