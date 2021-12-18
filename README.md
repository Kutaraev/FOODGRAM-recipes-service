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
![логин](https://lh3.googleusercontent.com/N6BdIGBy7PBrp3y24JKnM6cxLB3ao6orI2a93rYd1tNYLF5Xk671yS20NNODRB7NBIsMYkTvnGq-wlbbJd0smDa6WyeUj1nSG5z4XbkaeO5ENWacAFV6yNDVZFgfZtgysdMQETlcqaT3eRD8jjSTsbW_sJflu48TbzRRMki_N-BPx3HlCDPOVNfQ4nANIfBdQgUkdM7MZxD34fudqRcS8EEglpgUtLJesbkzM16mijXg4L0fV1pjLhDAu6DQV6N9ETbCcQVnPUuX_umRDqes8jEu5BMXUs1PRHviyjAbzze1Z_fBhGrEelnscBdvrhOT2EUqlNL0muNxAmNXAgzbrEM8crH4pHltpYqp7oI--zxOtd2WGnT6YHrHlr3v0pLG7RcRvtEajnYs0wfwzDG1jmF-tW3Tj52fmMIusDLLj5AYmtV_1LcUVkeUn0fblR3RLomsTUnAarKgAqYSYWBQhHtHfdDZo92W9AzJU2PCTCcLpvVPV-c8PbtF1FpH3KerDTRwHWxuUBHj9crO0DXr9GnflCNUAAtF8SOTW7BkHHOL-jtBT3odltVHwunnJXcbTqk-s9S1ySqgUJ4TbGMIqoUbdO6o94h3L1EJBGjLS7KCXzsBjOpPLTJ1KmwcdFnsTq5qCT7F-fRUyO0c3NGjYddSx76Yd56Is6ZCeVVrWudi9m6Vwa_tz4eNB-y7i-wzKDqO1NmYKj7iln60DF96dm-5=w958-h462-no?authuser=0)
### Форма регистрации нового пользователя
![регистрация](https://lh3.googleusercontent.com/JJVLIJdQaoS26mebZ-_Ukk-2sfP6KDh2G0n2rX_4Ns1zBlN8nZgwcc6v29rlfsaPztzxul1VTyRgeXe1pybX98fieX2J9Vua11iG93CGQJf2NbsWNnAo_RKy1x9lkJpDCeBgYCksUI--9RlckKxDh3aWVmkyfoGo3HWvqB3_CpSaElYyG5kUzPlBf4Y5yc4Ond86DNeuWc07uAsd-NDrwMeNfAKb018rBWrYWX8TsYXfohyHQgdxailm_8IldSrPxRhDofXaGjjG5ZYvGNjDS8QspRa7yzbNiuWH4CjMLNRr5_x0EYhiej60LVGGKjoYe4KMmj_e9rl76fPku38vjhXZmvuVouMbVqR0A4Tjwj4dDezQrAzF6DO54EgvxwGNRQFzHrFfGuB9850VepcCd5ySJVO5AHO4DR1CRbZKG44zxN2WW1f3Mj8gZ5rvios9odAzmfi3TZ2X-QUTIAIKQp2vHRBWGZdaEXeWJXXGvZDJhj3URDWIBrw0rZawVhYUGD-2eWJ9AuANTpleBYqrLKrgoIM2_Cv5ELJX-R4ksjOyawNHqtmjrHbQ0-DpZ86hKRzu-O0gXgIOWWEzWxKa6u67hG-cGkJnk8Ph-ecMmKsGjAqfDMe2DWF7lj_KUSLMWQYyUxRTIEa-VNXbnvgaQstH7AfWuQZyf95PZqskGuDzpH7f6TyqlTkKfnTurj0mUnAfUFoTT1NXvrprXfMmLGVj=w959-h653-no?authuser=0)
### Главная страница с рецептами
![главная страница](https://lh3.googleusercontent.com/o9gcXTbm_OyR0a08QRzoFAsbJmZTB_KFxApzULleZLMug4FIfdcsMZMO3iHSea9uywynkkPYYkaJ8fRToWaX-jEl9LtJlw0kaceipYhqDkb7Cwm9-IpfBcIAGRwodgBs6_lnqXI8pRG4vLkT78v9mkiwbK1ZjS288aKG4V42g4KbsnwoTY0ov5jgACDao99nWVWS1u3Uj5eXJG5RrRVRlrem0Azxf-t9wbOAg1GWXfRCsHdb00-Zc72uMf5bNroGmLVrvCgYqCo6oLfoehSgvXsXPeghPqIetNbr-eowIkMKabotsPKDjbivI9EvIlEFrKTBHAoD2edep5NvpyB3WAnoFOv7cR-ylc7U0CqTbObsDm17UCpiEDYIv723ztLTR6tqU4maO9cTZIdMwPeZGaucwTbJKSihbm9KAmOaJjLy6WxTf-QMZHJt23vhwPeDWEJhBz7ePN7fP1KV03Eh_sWKiG7sPphSlZ6beNRUQbyyMwSkWpGET9YRAL6w1wfc9WqrlQwYFz784dXcQO6F9hS0fx2VAWPffdurqVVU-Guv6d4DbIKPnzhExzdPI3--UDQw7s5QtwluXKE1CdhYp9NCu1bwx37c6mvdmDao8zJxoY8yn0TTjuuOCt0RvJX3lGhjCcNrJBx0keWpsgcsE3z9rC5KnZ6nov-UJoXPk_ACB0STxyPF9Sw_vddu_u-Wh_AQBtBfSUWWGEFehaQSLMEe=w959-h588-no?authuser=0)
### Окно создания рецепта
![создание рецепта](https://lh3.googleusercontent.com/9W_Y-HVDSUxVIt_Ad0Sok-SoPFEJAESOowj6UrG0B6sCqTQZhY-m8Mr2lvm-bZwHnbhEB2qDyxRJrVqRaX4_1xBP0oL8NnjXU1S26-sDLLsAWk4p_YFGjeMOt_KzxmD9NxMJbCJ_-j0YMtOnO6CE9lgvNzmDofBSIWL7J8hwYPlbIAiXWzUtcpBJSvDbKtWCb89qMthAbkwIX2JEUeQmkx3-ILxtn83h0d_pX4V4Yuz6f4Kpu0SDShdOAvSRYpGsr9-i0lBqvns2BfFzCYQKb22-2ly0W1dYRe5w29a9eOBoOocaNM0lu1mLfQ_EyJcjOayYhqwvMChxIc0DP0dL4jnTJkXL0h3BlWIDTBvablT8NM2_hYckgUJihJSnHgaEMwgAyrV9eFVfD5SdZG0P3Uvu9m-U2OqYLfNuSJoSJWuCOfbt2GGhZ9TiUmg0iAg70Ti7kwJCZ_oYReVS6K7e3oaLtHxmVougdthAkqmzLzqiaW6YrTO7ETZ_H7YI7dBh5mMv0u2_07-zrDO5UrgHXz5y5MpE5ksrMwvcuopSmTrtygHdKvz6a8nWBkaqVfRgq7cMissNwtk6SSCl0Qt0EkR9iYqnKrpMF3OSU6uyr4fobXF7tmmQV9hZTCDC8YNEQ86rjwmyA6rwv6ChkI1S4gKjQiPOENX5nm2NkpxO0l-nANUdNuNY5QYXHXMoP5uEY_xYmanOtjwX9DHkY1QvUtdm=w802-h782-no?authuser=0)
### Страница подписок
![подписки](https://lh3.googleusercontent.com/j8P-Ynqmk8k3vKt164bhQqqTO_IXgoAqrMU8-r8VyoQoscNI3SLcNAg-SX8TjjFPjBRkXN5VghaZQKLx0RDEdPhU2fT6ZGWtacGs3c4ThXPomgi2ooU3DEOLvqmli-OfjcavxTS2gyvWFhF3AUpc9OEqG4kpN3Z7YbhEkrSNlA6sQNbwL0fdqoakBR-sbCY3MxVkCyHQEinTb81kJ19YTCQbT0FA5s2YFotpUUEHNl-2DtdqDiJ8qh_mHkY92n1qoJggGk8gZZpJMrbOjD7VbiE0qZshIjwhODeeaIdIm8Ua0BaGmBLG91TpBr9NO3VLiWAPSIB0ShqNmR8YRjNb5xRNxuDiIq8G-4f9sXvX-_xrlYh3XC_4cfpt_5IJWhkS1Ev0U1qNl13oHaal_ENxDri8cDTh1zlhFSPSaKPLrIuXf0POCIx3yV85UyK0zPitjIq6Wdzh1CeJoFhFjDT-055p9OPG8MQiWiste4J4hf2Pj9fY845d-F9dBacT38hS98nrIEu5Ka7IY565An8iCC3Inb4iv1aXNU1-ay7zHIvl3K_YQIHPUO4w9pokX9xDemLsWOL8XTS5oLNNfR5xnWAWRk4sd2w7wBbNIGbKn-1agcheHTwjOvoqIutH8NzdKWIMQR1BMoyNvaoc5n6rpUfLdsAhrH-qmt2idDxtzV3z21Q_ZM3yNOzfNFofCLEwLCAP4tKyl6XxhLc2FjJitJ_A=w642-h443-no?authuser=0)
### Пример выгруженного списка покупок
![список покупок](https://lh3.googleusercontent.com/A2jatAwczgR-b4wEekWSRSa8gnuVjqHBMlJM7ndoLB6RcsIeX78RE6d_QGU0Nyat2_Q5m_GLa4_paNoJG31MUu4926nuydsJkpRzCf_I4R12pnjSARAeyq7BFH-JS5RlRjoVgTAme86XUwngq6eSyTmCQKz_Uypvns57bDO-sKstKYUvJu68ibhIA-jMLH5zh1-xgyMDFDyJ5WoCPUkIUrmCaSHxxK9ZtPoIsCvKoehKsy9fndub4Uu5SjV6EmyycI7rCHjSYoUEwCOeNbKXPY3dYE9WL_FxgCg1akRfj4ACywSpcpSJoA5uae8AlXt4Zyiq5ApA6mSkGu4UzqQmZT6aBa4_nTYbBSr1SaTXCvkoA5tKYu1wAabHT4eHuiNAgPunq8D3VGunLyK1idw5gfQ8i4q00NgyYMZxLNF9CR9UERe3XetCy-3duSImmjz9x8CXDh4l8PclYGGzvb6dl4sJcBYM5dChw60JT-UctFxb_IFMlRvOBrwfTF-p7srUr6YPkFM1kGJKzNoCWnGN4p6xu7fKdqheI0VXYbkgaSyJhCqBgj6XV7ucyKUE7NCRa4nQjImcQX3Z5x0WG6mWmJxPox4KEyXFYTgsbI_JWVn2eIhdVwao1l6AHRSSq1LG_aUxa84j4vv-i5nV7m0vyqQPlxR6NW850PaW0tkrQmitGxYa48lg1JJOr-aBKHkz6RHxYlH9V9h1dALg4cfcUAmL=w378-h497-no?authuser=0)

## <a name="Планы">Планы по развитию проекта</a>
1. Создание системы рейтингов для рецептов.
2. Возможность оставлять комментарии под рецептами.
3. Возможность разбивать рецепты по тематическим группам.
4. Добавление фильтрации по времени приготовления.
5. Создание системы поиска рецептов.

## <a name="Контакты">Контакты</a>
Артем Кутараев – [@artem_kutaraev](https://t.me/artem_kutaraev) – artem.kutaraev@gmail.com  
Ссылка на проект – [https://github.com/Kutaraev/FOODGRAM-recipes-service.git](https://github.com/Kutaraev/FOODGRAM-recipes-service.git)
