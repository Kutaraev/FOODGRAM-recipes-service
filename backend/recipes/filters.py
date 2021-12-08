from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter

from .models import Recipe


class RecipeFilter(filters.FilterSet):
    is_in_shopping_cart = filters.BooleanFilter(
        method='get_is_in_shopping_cart')
    is_favorited = filters.BooleanFilter(
        method='get_is_favorited')
    tags = filters.AllValuesMultipleFilter(
        field_name='tags__slug',
        lookup_expr='contains'
    )

    class Meta:
        model = Recipe
        fields = ['is_in_shopping_cart', 'author', 'is_favorited', 'tags']

    def get_is_in_shopping_cart(self, queryset, name, value):
        if value:
            return queryset.filter(shoplist__user=self.request.user)
        return queryset.all()

    def get_is_favorited(self, queryset, name, value):
        if value:
            return queryset.filter(favorite__user=self.request.user)
        return queryset.all()


class IngredientFilter(SearchFilter):
    search_param = 'name'
