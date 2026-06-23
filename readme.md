# 🎬 Film Web Service

Веб-приложение для управления фильмами с аутентификацией пользователей и системой закладок. Реализовано на Flask с использованием SQLAlchemy, REST API с автоматической документацией Swagger и JWT-аутентификацией.

## 📋 Содержание

- [Технологии](#-технологии)
- [Функциональность](#-функциональность)
- [Структура проекта](#-структура-проекта)
- [Требования](#-требования)
- [Установка и запуск](#-установка-и-запуск)
- [API Эндпоинты](#-api-эндпоинты)
- [Примеры использования](#-примеры-использования)
- [Возможные ошибки](#-возможные-ошибки)
- [Лицензия](#-лицензия)

---

## 🛠 Технологии

- **Python 3.14+** — язык программирования
- **Flask 3.0+** — веб-фреймворк
- **Flask-RESTx 1.3+** — для создания REST API с Swagger документацией
- **SQLAlchemy 2.0+** — ORM для работы с базой данных
- **Flask-SQLAlchemy 3.1+** — интеграция SQLAlchemy с Flask
- **Marshmallow 3.19+** — валидация и сериализация данных
- **PyJWT 2.13** — JWT аутентификация
- **SQLite 3** — база данных


---

## ✨ Функциональность

### 🔐 Аутентификация и пользователи
- ✅ Регистрация новых пользователей
- ✅ Вход в систему с получением JWT токенов (access + refresh)
- ✅ Обновление токенов по refresh токену
- ✅ Просмотр профиля пользователя
- ✅ Редактирование профиля (имя, фамилия, любимый жанр)
- ✅ Изменение пароля

### 🎬 Фильмы, жанры, режиссеры
- ✅ Получение списка всех фильмов с пагинацией
- ✅ Получение фильма по ID
- ✅ Сортировка фильмов по новизне
- ✅ Получение списка всех жанров
- ✅ Получение жанра по ID
- ✅ Получение списка всех режиссеров
- ✅ Получение режиссера по ID

### ❤️ Закладки (Favorites)
- ✅ Добавление фильма в закладки
- ✅ Удаление фильма из закладок
- ✅ Просмотр всех закладок пользователя

---

## 📁 Структура проекта

```
film_web_service/
├── app.py                 # Точка входа в приложение
├── config.py              # Конфигурация приложения
├── setup_db.py            # Инициализация базы данных
├── constants.py           # Константы приложения
├── implemented.py         # Вспомогательные функции
├── dao/                   # Data Access Objects
│   ├── director_dao.py
│   ├── genre_dao.py
│   ├── movie_dao.py
│   └── user_dao.py
├── service/               # Business Logic Layer
│   ├── auth_service.py
│   ├── director_service.py
│   ├── genre_service.py
│   ├── movie_service.py
│   └── user_service.py
├── views/                 # API Endpoints
│   ├── auth.py
│   ├── directors.py
│   ├── genres.py
│   ├── movies.py
│   └── users.py
├── helpers/               # Утилиты и помощники
├── Dockerfile             # Docker конфигурация
├── docker-compose.yaml    # Docker Compose конфигурация
├── requirements.txt       # Зависимости Python
└── movies.db              # SQLite база данных
```

---

## ⚙️ Требования

- **Python**: 3.8+
- **pip**: для установки зависимостей
- **Docker**: опционально для контейнеризации
- **Git**: для клонирования репозитория

---

## 🚀 Установка и запуск


```bash
docker compose up --build
```

Приложение будет доступно по адресу: `http://localhost:5000`  
Документация Swagger: `http://localhost:5000/docs/`

### Способ 2: Docker (вручную)

```bash
# Сборка образа
docker build -t film-web-service .

# Запуск контейнера
docker run --rm -p 5000:5000 film-web-service
```

### Способ 3: Локальное развертывание

#### 1. Клонирование репозитория
```bash
git clone https://github.com/your-username/film_web_service.git
cd film_web_service
```

#### 2. Создание виртуального окружения
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

#### 4. Запуск приложения
```bash
python app.py
```

Приложение будет доступно по адресу: `http://localhost:5000`

---

## 📚 API Эндпоинты


### 🔐 Аутентификация

| Метод | Эндпоинт | Описание | Авторизация |
|-------|----------|----------|---|
| POST | `/auth/register` | Регистрация нового пользователя | ❌ |
| POST | `/auth/login` | Вход в систему | ❌ |
| PUT | `/auth/refresh` | Обновление токенов | ❌ |

### 👤 Пользователи

| Метод | Эндпоинт | Описание | Авторизация |
|-------|----------|----------|---|
| GET | `/user/` | Получить профиль | ✅ |
| PATCH | `/user/` | Обновить профиль | ✅ |
| PUT | `/user/password` | Изменить пароль | ✅ |

### 🎬 Фильмы

| Метод | Эндпоинт | Описание | Авторизация |
|-------|----------|----------|---|
| GET | `/movies/` | Получить все фильмы | ❌ |
| GET | `/movies/{id}` | Получить фильм по ID | ❌ |

**Параметры пагинации и фильтрации:**
```
GET /movies/?page=1              # Страница 1 (12 фильмов)
GET /movies/?status=new          # Новинки (сортировка по году)
GET /movies/?page=2&status=new   # Новинки, страница 2
```

### 🎭 Жанры

| Метод | Эндпоинт | Описание | Авторизация |
|-------|----------|----------|---|
| GET | `/genres/` | Получить все жанры | ❌ |
| GET | `/genres/{id}` | Получить жанр по ID | ❌ |

### 🎥 Режиссеры

| Метод | Эндпоинт | Описание | Авторизация |
|-------|----------|----------|---|
| GET | `/directors/` | Получить всех режиссеров | ❌ |
| GET | `/directors/{id}` | Получить режиссера по ID | ❌ |

### ❤️ Закладки

| Метод | Эндпоинт | Описание | Авторизация |
|-------|----------|----------|---|
| GET | `/user/favorites/` | Получить все закладки | ✅ |
| POST | `/user/favorites/{movie_id}` | Добавить в закладки | ✅ |
| DELETE | `/user/favorites/{movie_id}` | Удалить из закладок | ✅ |

---

## 🔑 JWT Авторизация

Для доступа к защищенным эндпоинтам необходимо передавать JWT токен в заголовке:

```
Authorization: Bearer <access_token>
```

**Пример:**
```bash
curl -X GET http://localhost:5000/user/ \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIs..."
```

---

## 💡 Примеры использования

### Регистрация

```bash
curl -X POST http://localhost:5000/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "secure_password"
  }'
```

**Ответ:**
```json
{
    "email": "user@example.com",
    "id": 1
}
```

### Вход в систему

```bash
curl -X POST http://localhost:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "secure_password"
  }'
```

**Ответ:**
```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIs..."
}
```

### Получение профиля

```bash
curl -X GET http://localhost:5000/user/ \
  -H "Authorization: Bearer <access_token>"
```

### Обновление профиля

```bash
curl -X PATCH http://localhost:5000/user/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Иван",
    "surname": "Петров",
    "favorite_genre": 1
  }'
```

### Получение фильмов

```bash
# Все фильмы
curl -X GET http://localhost:5000/movies/

# С пагинацией
curl -X GET "http://localhost:5000/movies/?page=1"

# Новинки
curl -X GET "http://localhost:5000/movies/?status=new"
```

### Добавление фильма в закладки

```bash
curl -X POST http://localhost:5000/user/favorites/1 \
  -H "Authorization: Bearer <access_token>"
```

---

## 📝 Работа с Swagger

После запуска приложения откройте в браузере:

```
http://localhost:5000/docs/
```

Здесь вы сможете:
- 📖 Просмотреть всю документацию API
- 🧪 Тестировать эндпоинты прямо из браузера
- 🔍 Увидеть схемы запросов и ответов
- 🔑 Введить JWT токен для авторизации

---

## 🐛 Возможные ошибки и их решение

### Ошибка `AssertionError: View function mapping is overwriting...`

**Причина:** Двойная инициализация Api в `app.py`.

**Решение:** Исправьте `register_extensions`:

```python
def register_extensions(app):
    db.init_app(app)
    api = Api(app)  # Только одна инициализация
    # Не вызывайте api.init_app(app) повторно!
    api.add_namespace(director_ns)
    # ...
```

### Ошибка `sqlalchemy.exc.UnmappedInstanceError`

**Причина:** Попытка добавить в сессию словарь вместо объекта модели.

**Решение:** Создавайте объекты моделей:

```python
# ❌ Неправильно
user_data = {'email': 'test@test.com'}
db.session.add(user_data)

# ✅ Правильно
user = User(email='test@test.com')
db.session.add(user)
```

### Ошибка `ExpiredSignatureError`

**Причина:** Истек срок действия токена.

**Решение:** Используйте refresh token для получения нового access token:

```bash
curl -X PUT http://localhost:5000/auth/refresh \
  -H "Content-Type: application/json" \
  -d '{
    "refresh_token": "<your_refresh_token>"
  }'
```

### Ошибка подключения к БД

**Причина:** База данных не инициализирована или неправильный путь в `config.py`.

**Решение:**
```python
# Убедитесь, что переменная SQLALCHEMY_DATABASE_URI корректна
# в config.py
SQLALCHEMY_DATABASE_URI = f'sqlite:///{path_db}'
```

---

## 📦 Структура данных

### Genre (Жанр)
```json
{
    "id": 1,
    "name": "Драма"
}
```

### Director (Режиссер)
```json
{
    "id": 1,
    "name": "Квентин Тарантино"
}
```

### Movie (Фильм)
```json
{
    "id": 1,
    "title": "Криминальное чтиво",
    "description": "...",
    "trailer": "https://...",
    "year": 1994,
    "rating": 8.9,
    "genre_id": 1,
    "director_id": 1
}
```

### User (Пользователь)
```json
{
    "id": 1,
    "email": "user@example.com",
    "name": "Иван",
    "surname": "Петров",
    "favorite_genre": 1
}
```

### Favorite (Закладка)
```json
{
    "id": 1,
    "user_id": 1,
    "movie_id": 1
}
```

---

## 📊 Дополнительная информация

### Пагинация

Все эндпоинты, возвращающие список, поддерживают пагинацию:

```bash
GET /movies/?page=1           # Первая страница (12 фильмов)
GET /movies/?page=2           # Вторая страница
GET /genres/?page=1           # Жанры со второй страницы
```

### Переменные окружения

Основные переменные в `config.py`:

```python
SECRET_HERE = '249y823r9v8238r9u'              # Секретный ключ для JWT
SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'  # Путь к БД
DEBUG = True                                      # Режим разработки
```

---

## 🛡️ Безопасность

- **Пароли:** Хешируются перед сохранением в БД
- **JWT токены:** Используются для аутентификации
- **CORS:** Можно настроить для разрешения запросов с других доменов
- **HTTPS:** Рекомендуется использовать в продакшене

---

## 📋 Требования к окружению

- **Python:** 3.8+
- **Flask:** 2.0+
- **SQLite:** встроена в Python
- **pip:** для управления зависимостями

---

## 🚢 Деплой

### На Heroku

```bash
heroku create your-app-name
git push heroku main
heroku open
```

### На VPS

```bash
# Скопируйте проект на сервер
scp -r . user@server:/path/to/project

# Установите зависимости
pip install -r requirements.txt

# Запустите через Gunicorn
gunicorn app:app
```

---

## 📝 Лицензия

Этот проект распространяется под лицензией MIT.

---

## 👨‍💻 Разработка

### Запуск в режиме разработки

```bash
python app.py
```

Сервер перезагружается автоматически при изменении файлов.

### Запуск с отладкой

```bash
export FLASK_ENV=development  # Linux/Mac
set FLASK_ENV=development     # Windows

python app.py
```

### Пример создания нового эндпоинта

1. Создайте файл в `views/`:
```python
from flask_restx import Namespace, Resource

books_ns = Namespace('books', description='Books API')

@books_ns.route('/')
class BookList(Resource):
    def get(self):
        """Get all books"""
        return {'books': []}

    def post(self):
        """Add new book"""
        return {'status': 'created'}, 201
```

2. Зарегистрируйте в `app.py`:
```python
from views.books import books_ns

# In register_extensions():
api.add_namespace(books_ns)
```

---
