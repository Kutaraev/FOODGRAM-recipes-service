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
- [Примеры страниц приложения](#Примеры)
- [Планы по развитию проекта](#Планы)
- [Контакты](#Контакты)

## <a name="Описание">Описание</a>
Минималистичный, но функциональный веб-сервис для публикации кулинарных рецептов. Пользователи могут регистрироваться и создавать рецепты. Так же они могут подписываться на других авторов, добавлять рецепты в избранное ив список покупок (с возможностью выгрузки списка в pdf-файл). Бекенд взаимодействует с фронтендом, написанном на React'e, при помощи API. Проект является масштабируемым и легко может быть дополнен необходимыми функциями.


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
![логин](https://i.postimg.cc/LXLWTfVj/image.png)
### Форма регистрации нового пользователя
![регистрация](https://i.postimg.cc/Prt7WCv8/image.png)
### Главная страница с рецептами
![главная страница](https://i.postimg.cc/k5kZKwWn/image.png)
### Окно создания рецепта
![создание рецепта](https://i.postimg.cc/jq69nH2b/image.png)
### Страница подписок
![подписки](https://i.postimg.cc/PJMRGj9x/image.png)
### Пример выгруженного списка покупок
![список покупок](https://i.postimg.cc/d3FxS1Wp/image.png)

## <a name="Планы">Планы по развитию проекта</a>
1. Создание системы рейтингов для рецептов.
2. Возможность оставлять комментарии под рецептами.
3. Возможность разбивать рецепты по тематическим группам.
4. Добавление фильтрации по времени приготовления.
5. Создание системы поиска рецептов.

## <a name="Контакты">Контакты</a>
Артем Кутараев – [@artem_kutaraev](https://t.me/artem_kutaraev) – artem.kutaraev@gmail.com  
Ссылка на проект – [https://github.com/Kutaraev/FOODGRAM-recipes-service.git](https://github.com/Kutaraev/FOODGRAM-recipes-service.git)
