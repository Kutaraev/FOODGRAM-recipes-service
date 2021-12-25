![yamdb_workflow](https://github.com/EvgeniyBudaev/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)  

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)


# Foodgram recipes service
Онлайн-сервис для публикации рецептов.

## Содержание
- [Описание проекта](#Описание)
- [Технологии](#Технологии)
- [Установка](#Установка)
- [Создание суперпользователя](#Админ)
- [API](#API)
- [Элементы интерфейса](#Примеры)
- [Планы по развитию проекта](#Планы)
- [Контакты](#Контакты)

## <a name="Описание">Описание</a>
Минималистичный, но функциональный веб-сервис для публикации кулинарных рецептов. Пользователи могут регистрироваться и создавать рецепты. Так же они могут подписываться на других авторов, добавлять рецепты в избранное и в список покупок (с возможностью выгрузки списка в pdf-файл). Бекенд взаимодействует с фронтендом, написанном на React'e, при помощи API. Проект является масштабируемым и легко может быть дополнен необходимыми функциями.


## <a name="Технологии">Технологии</a>
- [Python 3](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [NGINX](https://nginx.org/)
- [Gunicorn](https://gunicorn.org/)
- [Git](https://github.com/)
- [Visual Studio Code](https://code.visualstudio.com/Download)

## <a name="Установка">Установка</a>

- Установите Docker на ваш сервер:
```
 sudo apt install docker.io
```

- Установите Docker-compose на сервер:
```
 sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
 sudo chmod +x /usr/local/bin/docker-compose
```

- Скопируйте на сервер файлы Docker-compose.yml и nginx.conf из папки infra-deploy/.

- Запустите контейнеры с помощью команды:
```
 docker-compose up
```

- Собрать статические файлы:
```
  docker-compose exec backend python3 manage.py collectstatic --noinput
```

- Произвести миграции:
```
 docker-compose exec backend python manage.py makemigrations
 docker-compose exec backend python manage.py migrate --noinput
```

- Загружаем ингредиенты в базу данных:
```
 docker-compose exec backend python manage.py loaddata dump.json
```

- Запуск контейнеров выполняется командой:
```
 docker-compose up
```

## <a name="Админ">Создание суперпользователя</a>
Для создания суперпользователя нужно ввести в терминале команду
```
docker-compose exec backend python manage.py createsuperuser
```
и ввести следующие данные:
- адрес электонной почты
- юзернейм
- имя
- фамилию
- пароль  

Теперь можно запустить docker-compose, зайти на адрес `http://127.0.0.1/admin/`, залогиниться и работать с админкой Django.

## <a name="API">API</a>
Перечень эндпоинтов, а также формат и вид данных находятся по адресу `http://127.0.0.1/api/docs/`

## <a name="Примеры">Элементы интерфейса</a>
В данном разделе показаны базовые элементы интерфейса сервиса "Продуктовый помощник"
### Окно входа на сайт
![логин](https://lh3.googleusercontent.com/hVdKRcQ5GVvgBRZTCTSMIVGSEn5ja2Zp9aFGghQq3T_JsKdYP2erjKJTMuvt6LT_UHNLtTJO4XIf649nhgM=w457-h220-rw)
### Форма регистрации нового пользователя
![регистрация](https://lh3.googleusercontent.com/0oBp0n7Dk2qXCarK5T68SMQoAcu0YKOa4QESKZ-yARqF0JsDN4iwPbzyKV-AUZY28CPTqmUAeIbOSDRPjsg=w323-h220-rw)
### Главная страница с рецептами
![главная страница](https://lh3.googleusercontent.com/WKlQCKhlguKfKoG3pkwVqxhNjJj6HzKLzDpMOvyYf_5FRr_PG1uIx4h3_TZzendePlaMIo4LBnTCWg4bbp0=w359-h220-rw)
### Окно создания рецепта
![создание рецепта](https://lh3.googleusercontent.com/69QPNgMUVfwLH-K7SCFumWW_ULFKcRBtMgjXdoy9a8qyxRVaMlloBRMC1nqG0UOSgqaj0tUJqPbDoE7ESpc=w226-h220-rw)
### Страница подписок
![подписки](https://lh3.googleusercontent.com/OeLU7KmLulfVprY-v9vNW1uK0airAZQybf8wyf2HKJGMsnlw2DYnUGqWs6mcJiZjZ6zAjQE2x7Qd9fLgUIs=w319-h220-rw)
### Пример выгруженного списка покупок
![список покупок](https://lh3.googleusercontent.com/SXP-efU0mk1XHgPldluPzzyfs789GOEA2ONfIY4RmbhtDA1A8bEUQIzXWrM05dARtK7k0v94vtAMPJy9R5s=w167-h220-rw)

## <a name="Планы">Планы по развитию проекта</a>
1. Создание системы рейтингов для рецептов.
2. Возможность оставлять комментарии под рецептами.
3. Возможность разбивать рецепты по тематическим группам.
4. Добавление фильтрации по времени приготовления.
5. Создание системы поиска рецептов.

## <a name="Контакты">Контакты</a>
Артем Кутараев – [@artem_kutaraev](https://t.me/artem_kutaraev) – artem.kutaraev@gmail.com  
Ссылка на проект – [https://github.com/Kutaraev/FOODGRAM-recipes-service.git](https://github.com/Kutaraev/FOODGRAM-recipes-service.git)
