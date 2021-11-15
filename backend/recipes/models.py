from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Recipe(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name="Автор рецепта",
        related_name='recipes'
    )
    name = models.CharField(max_length=100)
    text = models.TextField()
    ingredients = models.ManyToManyField(
        'Ingredient',
        through='Amount'
    )
    tags = models.ManyToManyField('Tag')
    cooking_time = models.PositiveSmallIntegerField()
    is_favorited = models.BooleanField(default=False)
    is_in_shopping_cart = models.BooleanField(default=False)
    image = models.BooleanField(default=False)


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    measurement_unit = models.CharField(max_length=100)


class Amount(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    amount = models.SmallIntegerField()


class Tag(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'color', 'slug'],
                name='unique_tag'
            )
        ]


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='follower',
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='following',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_follow'
            )
        ]


class Favorite(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
     )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
