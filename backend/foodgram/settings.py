import os
from pathlib import Path

import environ

env = environ.Env()
environ.Env.read_env()


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = ('django-insecure-sb%3+zsmt5&58' +
              '*6qna)kuv_drk++vy!5lhnq-30wn(r@#9z5p1')


DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'users.User'


INSTALLED_APPS = [
    'foodgram',
    'users',
    'recipes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'djoser',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'foodgram.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'foodgram.wsgi.application'


DATABASES = {
    'default': env.db()
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.'
        'UserAttributeSimilarityValidator',
     },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],

    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ]
}


DJOSER = {
    "SERIALIZERS": {
        "user": "users.serializers.CustomUserSerializer",
        "current_user": "users.serializers.CustomUserSerializer",
    },

    "PERMISSIONS": {
        'user': ['rest_framework.permissions.AllowAny'],
        'user_list': ['rest_framework.permissions.IsAdminUser'],
        'current_user': ['rest_framework.permissions.IsAuthenticated'],
    },
}


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
