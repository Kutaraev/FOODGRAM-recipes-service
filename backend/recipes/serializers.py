from rest_framework import serializers

from users.serializers import CustomUserSerializer

from .models import Amount, Favorite, Follow, Ingredient, Recipe, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')


class AmountSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(source='ingredient.id')
    name = serializers.ReadOnlyField(source='ingredient.name')
    measurement_unit = serializers.ReadOnlyField(
        source='ingredient.measurement_unit'
    )

    class Meta:
        model = Amount
        fields = ('id', 'name', 'measurement_unit', 'amount')


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')


class RecipeSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    ingredients = AmountSerializer(
        source='amount_set', many=True, read_only=True
    )
    tags = TagSerializer(read_only=True, many=True)

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

    def create(self, validated_data):
        ingredients = self.initial_data['ingredients']
        tags = self.initial_data['tags']
        user = self.context['request'].user
        recipe = Recipe.objects.create(
            author=user,
            **validated_data)
        for ingredient in ingredients:
            Amount.objects.create(
                recipe=recipe,
                ingredient=Ingredient(id=ingredient['id']),
                amount=ingredient['amount']
            )
        recipe.tags.add(*tags)
        return recipe


class UserRecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('id',
                  'name',
                  'image',
                  'text',)


class FollowSerializer(serializers.ModelSerializer):
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


class ShoppingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('id',
                  'name',
                  'image',
                  'cooking_time',
                  'is_in_shopping_cart')
