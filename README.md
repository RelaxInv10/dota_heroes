# Dota Heroes

**Dota Heroes** — веб-приложение на Django, посвящённое героям игры Dota 2.

Проект разработан для изучения Python Backend-разработки, работы с Django ORM, базами данных и HTML-шаблонами.

## Возможности

- Просмотр каталога героев Dota 2.
- Просмотр подробной информации о каждом герое.
- Отображение основных атрибутов и игровых позиций.
- Управление героями, атрибутами и позициями через Django Admin.
- Главная страница, новости и информация о проекте.

## Технологии

- **Python**
- **Django 6.1.1**
- **SQLite**
- **HTML5**
- **CSS3**
- **Django ORM**
- **Git / GitHub**

## Установка и запуск

**1. Клонируйте репозиторий**

```bash
git clone https://github.com/kazarinovmaxim-wq/dota_heroes.git
cd dota_heroes
```

**2. Создайте виртуальное окружение**

```bash
python -m venv venv
```

Активация для Windows:

```bash
venv\Scripts\activate
```

**3. Установите зависимости**

```bash
pip install -r requirements.txt
```

**4. Создайте файл `.env` в корне проекта**

```env
DJANGO_SECRET_KEY=your-generated-django-secret-key
DJANGO_DEBUG=True
```

Для генерации ключа Django можно выполнить:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**5. Примените миграции**

```bash
python manage.py migrate
```

**6. Запустите сервер**

```bash
python manage.py runserver
```

Откройте в браузере:

http://127.0.0.1:8000/

> Примечание: локальная база данных не включена в репозиторий. После установки необходимо самостоятельно добавить героев через Django Admin.

## Структура проекта

- `description/` — модели, представления и маршруты героев.
- `page/` — основные страницы сайта.
- `dota_main/` — настройки Django.
- `templates/` — HTML-шаблоны.
- `static/` — CSS-стили и изображения.

## Автор

**Maxim Kazarinov**

Начинающий Python Backend-разработчик.

GitHub: https://github.com/kazarinovmaxim-wq