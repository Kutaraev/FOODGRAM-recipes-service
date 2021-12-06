# Foodgram
Ваш продуктовый помощник
## Описание
Данный проект представляет собой онлайн-сервис для публикации кулинарных рецептов и API для него.
## Ссылка на работающий проект
http://84.201.138.107/recipes
## Перечень технологий, используемых в проекте
1. Python 3.8.4
2. Django 3.2.9
3. Pillow 8.4.0
4. Djangorestframework 3.12.4
5. Psycopg2-binary 2.9.1
6. Djoser 2.1.0
7. Gunicorn 20.0.4
8. NGINX 1.18.0
9. Docker 20.10.8
10. Visual Studio Code
## Установка

1. Установите Docker на ваш компьютер.

2. Скачать необходимые образы с Docker Hub
   (Внимание: Docker должен быть установлен на вашем компьютере)
 ```
    docker pull kutaraev/db:v1.0
    docker pull kutaraev/backend:v1.0
    docker pull kutaraev/frontend:v1.0
    docker pull kutaraev/nginx:v1.0
```
3. Создать переменную окружения .env со следющими значениями:
   SECRET_KEY;
   DATABASE_URL.

4. Запустить Docker-compose
 ```
    docker docker-compose up
```

## Создание суперпользователя
Для создания суперпользователя нужно ввести в терминале комнду
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

## API
Перечень эндпоинтов, а твкже формат и вид данных находятся по адресу `http://127.0.0.1/api/docs/`

## Элементы интерфейса
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
