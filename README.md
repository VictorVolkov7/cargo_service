# **Cargo service**

Это проект, написанный на языках 

- Python 3.11

С использованием библиотек/фреймворков:
- Django 55.0.3
- Django REST framework 3.15.1
- drf-spectacular 0.27.1
- PostgreSQL 
- Redis 5.0.3
- Celery 5.3.6
- Celery beat 2.6.0

Сервис поиска ближайших машин для перевозки грузов с API интерфейсом и админ-панелью.


## **Установка**
### Для установки проекта Electronic sales, следуйте инструкциям ниже:

**<p>1. Сделайте Fork этого репозитория. Репозиторий появится в ваших личных репозиториях на GitHub.</p>**

**1.1 Сделайте `git clone` форкнутого репозитория, чтобы получить репозиторий локально:**

**<p>2. Перейдите в папку с проектом.</p>**

**<p>3. Создайте и активируйте виртуальное окружение:</p>**

`poetry init`

`poetry shell`

**<p>4. Установите зависимости проекта:</p>**

`poetry install`

**<p>5. Создайте файл .env в корневой папке проекта (nearest_car/) и заполните данные для настройки проекта из файла .env.sample:</p>**

```ini
/.env/

# Django setting
DJANGO_SECRET_KEY=django secret key
REDIS_URL=redis url, default redis://localhost:6379

# PostgreSQL connection
POSTGRES_DB=db name
POSTGRES_USER=psql username
POSTGRES_PASSWORD=psql password
POSTGRES_HOST=host for db
POSTGRES_PORT=port for db

# superuser creation
SU_EMAIL=superuser email
SU_PASSWORD=superuser password
```

**<p>6. Примените миграции:</p>**

`python manage.py migrate`

**<p>7. Воспользуйтесь командой для установки русского языка:</p>**

`django-admin compilemessages`

**<p>8. ЗАПУСК BACKEND-ЧАСТИ: Запустите сервер:</p>**

`python manage.py runserver` или настройте запуск Django сервера в настройках.


Таким образом можно работать с backend-частью локально для отладки.

После запуска сервера. Вы сможете перейти на сайт с документацией http://127.0.0.1:8000/api/docs/ 
(если сервер запущен локально), и начать пользоваться всеми API методами проекта. 

Также вы можете схему данных .yaml файлом по адресу http://127.0.0.1:8000/api/schema/ (если сервер запущен локально).

### Либо с помощью Docker
**<p>1. Создайте файл .env.docker в корневой папке проекта (nearest_car/) и заполните данные для настройки проекта из файла .env.sample.docker:</p>**
```ini
/.env.docker/

# Django setting
DJANGO_SECRET_KEY=your django secret key
REDIS_URL=redis url, default redis://redis:6379

# PostgreSQL connection
POSTGRES_DB=database name
POSTGRES_USER=postgresql username
POSTGRES_PASSWORD=postgresql password
POSTGRES_HOST=container name
POSTGRES_PORT=your port

# superuser creation
SU_EMAIL=superuser email
SU_PASSWORD=superuser password
```

**<p>2. ЗАПУСК BACKEND-ЧАСТИ:: Воспользуйтесь командами:</p>**

`docker compose build` для создания оптимального билда проекта.

`docker compose up` для запуска docker compose контейнера.




## **Использование**
#### На проекте реализована регистрация новых пользователей через django админ-панель или API.
Также есть команда для создания суперпользователя `python manage.py csu` с данными из .env файла

#### Для тестирования вы можете заполнить базу данных данными из фикстур при помощи команд 
`python manage.py load_fixtures`
и `python manage.py fill_cars`

Либо создать свои через django админ-панель или API. (Через docker команды выполняются автоматически)




Автор
VictorVolkov7 - vektorn1212@gmail.com