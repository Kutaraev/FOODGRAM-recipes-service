from django.conf import settings
from django.core import validators
from django.db import models

User = settings.AUTH_USER_MODEL


class Recipe(models.Model):
    """Модель для создания рецептов"""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор рецепта',
        related_name='recipes'
    )
    name = models.CharField(max_length=100, verbose_name='Название рецепта')
    text = models.TextField(verbose_name='Описание рецепта')
    ingredients = models.ManyToManyField(
        'Ingredient',
        through='Amount',
        verbose_name='Ингредиенты'
    )
    tags = models.ManyToManyField('Tag', related_name='recipes',
                                  verbose_name='Теги')
    cooking_time = models.PositiveSmallIntegerField(
        validators=(
            validators.MinValueValidator(
                1, message='Нельзя прикотовить быстрее, чем за минуту'),),
        verbose_name='Время приготовления')
    image = models.ImageField(verbose_name='Фото')
    created = models.DateTimeField('date published',
                                   auto_now_add=True,
                                   verbose_name='Дата создания')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Модель ингредиентов"""
    name = models.CharField(max_length=100, verbose_name='Название тега')
    measurement_unit = models.CharField(max_length=100,
                                        verbose_name='Время приготовления')

    class Meta:
        ordering = ['id']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Amount(models.Model):
    """Модель для количества конкретного ингредиента"""
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE,
                               verbose_name='Рецепт')
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE,
                                   verbose_name='Ингредиент')
    amount = models.PositiveSmallIntegerField(
        validators=(
            validators.MinValueValidator(
                1, message='Минимальное количество - 1'),),
        verbose_name='Количество ингридиента',
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Количество ингредиентов в рецепте'
        verbose_name_plural = 'Количество ингредиентов в рецепте'


class Tag(models.Model):
    """Модель для тегов"""
    name = models.CharField(max_length=100, verbose_name='Название тега')
    color = models.CharField(max_length=100, verbose_name='Цвет тега')
    slug = models.SlugField(unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'color', 'slug'],
                name='unique_tag'
            )
        ]

    def __str__(self):
        return self.slug


class Follow(models.Model):
    """Модель для создания подписок на пользователей"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор'
    )

    class Meta:
        verbose_name = 'Подписки'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_follow'
            )
        ]


class Favorite(models.Model):
    """Модель для добавления рецептов в избранное"""
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, verbose_name='Рецепт'
     )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        constraints = [
            models.UniqueConstraint(fields=['recipe', 'user'],
                                    name='unique_favorite')
        ]


class ShopList(models.Model):
    """Модель продуктовой корзины"""
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, verbose_name='Рецепт'
     )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Продуктовая корзина'
        verbose_name_plural = 'Продуктовая корзина'
        constraints = [
            models.UniqueConstraint(fields=['recipe', 'user'],
                                    name='unique_product_cart')
        ]
