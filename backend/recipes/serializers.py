from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from users.serializers import CustomUserSerializer
from .models import Amount, Favorite, Follow, Ingredient, Recipe, ShopList, Tag


class TagSerializer(serializers.ModelSerializer):
    """Сериализатор тегов"""
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')


class AmountSerializer(serializers.HyperlinkedModelSerializer):
    """Сериализатор количества ингредиентов"""
    id = serializers.ReadOnlyField(source='ingredient.id')
    name = serializers.ReadOnlyField(source='ingredient.name')
    measurement_unit = serializers.ReadOnlyField(
        source='ingredient.measurement_unit'
    )

    class Meta:
        model = Amount
        fields = ('id', 'name', 'measurement_unit', 'amount')


class IngredientSerializer(serializers.ModelSerializer):
    """Общий сериализатор для ингредиентов"""
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')


class RecipeSerializer(serializers.ModelSerializer):
    """Сериализатор рецептов"""
    image = Base64ImageField()
    author = CustomUserSerializer(read_only=True)
    ingredients = AmountSerializer(
        source='amount_set', many=True, read_only=True
    )
    tags = TagSerializer(read_only=True, many=True)
    is_in_shopping_cart = serializers.SerializerMethodField()
    is_favorited = serializers.SerializerMethodField(
        read_only=True, default=False
    )

    class Meta:
        model = Recipe
        fields = ('id',
                  'tags',
                  'author',
                  'ingredients',
                  'is_favorited',
                  'is_in_shopping_cart',
                  'name',
                  'image',
                  'text',
                  'cooking_time',)

    def update_ingredients(self, ingredients, recipe):
        for ingredient in ingredients:
            Amount.objects.create(
                recipe=recipe,
                ingredient_id=ingredient.get('id'),
                amount=ingredient.get('amount'),
            )

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')
        tags = validated_data.pop('tags')
        user = self.context['request'].user
        recipe = Recipe.objects.create(
            author=user,
            **validated_data)
        self.update_ingredients(ingredients, recipe)
        recipe.tags.set(tags)
        return recipe

    def update(self, recipe, validated_data):
        if 'ingredients' in self.initial_data:
            ingredients = validated_data.pop('ingredients')
            recipe.ingredients.clear()
            self.update_ingredients(ingredients, recipe)
        if 'tags' in self.initial_data:
            tags = validated_data.pop('tags')
            recipe.tags.set(tags)
        return super().update(recipe, validated_data)

    def get_is_in_shopping_cart(self, obj):
        user = self.context.get('request').user
        if user.is_anonymous:
            return False
        return ShopList.objects.filter(recipe=obj, user=user).exists()

    def get_is_favorited(self, obj):
        user = self.context.get('request').user
        if user.is_anonymous:
            return False
        return Favorite.objects.filter(recipe=obj, user=user).exists()

    def validate(self, data):
        tags = self.initial_data.get('tags')
        if not tags:
            raise serializers.ValidationError(
                'Добавьте как минимум один тег'
            )
        if len(tags) != len(set(tags)):
            raise serializers.ValidationError('Теги должны быть уникальными!')
        data['tags'] = tags
        ingredients = self.initial_data.get('ingredients')
        if not ingredients:
            raise serializers.ValidationError(
                'Добавьте ингредиенты для рецепта'
            )
        unique_ingredients = []
        for ingredient in ingredients:
            ingredient_id = ingredient.get('id'),
            if int(ingredient['amount']) <= 0:
                raise serializers.ValidationError(
                    'Кол-во ингредиента должно быть больше 0'
                )
            unique_ingredients.append(ingredient_id)
        if len(unique_ingredients) != len(set(unique_ingredients)):
            raise serializers.ValidationError(
                'Ингредиенты должны быть уникальными!'
            )
        data['ingredients'] = ingredients
        cooking_time = self.initial_data.get('cooking_time')
        if int(cooking_time) <= 0:
            raise serializers.ValidationError(
                'Убедитесь, что время приготовления больше нуля'
            )
        return data


class UserRecipeSerializer(serializers.ModelSerializer):
    """Сериализатор для списка рецептов конкретного пользователя"""
    class Meta:
        model = Recipe
        fields = ('id',
                  'name',
                  'image',
                  'text',)


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор подписок"""
    email = serializers.ReadOnlyField(source='following.email')
    id = serializers.ReadOnlyField(source='following.id')
    username = serializers.ReadOnlyField(source='following.username')
    first_name = serializers.ReadOnlyField(source='following.first_name')
    last_name = serializers.ReadOnlyField(source='following.last_name')
    is_subscribed = serializers.ReadOnlyField(source='following.is_subscribed')
    recipes = serializers.SerializerMethodField()
    recipes_count = serializers.SerializerMethodField()

    class Meta:
        model = Follow
        fields = ('email',
                  'id',
                  'username',
                  'first_name',
                  'last_name',
                  'is_subscribed',
                  'recipes',
                  'recipes_count')

    def get_recipes(self, obj):
        user_recipes = Recipe.objects.filter(author=obj.following.id)
        return UserRecipeSerializer(user_recipes, many=True).data

    def get_recipes_count(self, obj):
        return Recipe.objects.filter(author=obj.following.id).count()


class FavoriteSerializer(serializers.ModelSerializer):
    """Сериализатор избранного"""
    id = serializers.ReadOnlyField(source='recipe.id')
    name = serializers.ReadOnlyField(source='recipe.name')
    image = serializers.ReadOnlyField(source='recipe.image')
    cooking_time = serializers.ReadOnlyField(source='recipe.cooking_time')

    class Meta:
        model = Favorite
        fields = ('id',
                  'name',
                  'image',
                  'cooking_time')


class MinRecipeSerializer(serializers.ModelSerializer):
    """Сериализатор выдает только необходимые поля."""
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')
        read_only_fields = ('id', 'name', 'image', 'cooking_time')
