from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


# Если оставить просто UserManager, то код не будет работать.
# Как я понял это имя определяет спец. тип объектов-менеджеров.
# и поэтому если оставить UserManager,
# то строка "objects = UserManager()" - не заработает.
class CustomUserManager(BaseUserManager):
    """Менеджер пользователей"""
    def create_user(self,
                    email,
                    username,
                    first_name,
                    last_name,
                    password=None):

        if not email:
            raise ValueError('Поле Email обязательно для заполнения')
        if not username:
            raise ValueError('Поле username обязательно для заполнения')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,
                         email,
                         username,
                         first_name,
                         last_name,
                         password=None):

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    """Кастомная модель пользователя"""
    email = models.EmailField(
        verbose_name='email',
        max_length=100,
        unique=True
    )
    username = models.CharField(max_length=50, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date_joined',
        auto_now_add=True
    )
    last_login = models.DateTimeField(
        verbose_name='last_login',
        auto_now_add=True
    )
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_subscribed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
