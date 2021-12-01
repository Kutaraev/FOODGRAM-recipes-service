from django.contrib import admin

from recipes.models import (Amount, Favorite, Follow, Ingredient, Recipe,
                            ShopList, Tag)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)
    search_fields = ['name']
    empty_value_display = "-пусто-"


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    empty_value_display = "-пусто-"


class ShopListAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    empty_value_display = "-пусто-"


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    empty_value_display = "-пусто-"


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')
    empty_value_display = "-пусто-"


class AmountInline(admin.TabularInline):
    model = Amount
    extra = 1


class AmountAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')
    empty_value_display = "-пусто-"


class RecipeAdmin(admin.ModelAdmin):
    inlines = (AmountInline,)
    list_display = ('author', 'name', 'favorite_count')
    list_filter = ('author', 'name', 'tags')
    search_fields = ['name']
    empty_value_display = "-пусто-"

    def favorite_count(self, obj):
        return Favorite.objects.filter(recipe=obj).count()


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(ShopList, ShopListAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Amount, AmountAdmin)
admin.site.register(Recipe, RecipeAdmin)
