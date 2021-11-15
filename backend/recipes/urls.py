from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (FavoriteViewSet, FollowersViewSet, IngredientViewSet,
                    RecipeViewSet, ShoppingListViewSet, TagViewSet, favorite,
                    hello)

router = SimpleRouter()
router.register('ingredients', IngredientViewSet)
router.register('recipes', RecipeViewSet)
router.register('tags', TagViewSet)

# Переделать через роутер
router.register(
    "users/subscriptions",
    FollowersViewSet,
    basename="Followers"
)

# Переделать через роутер
router.register(
    "users/favorites",
    FavoriteViewSet,
    basename="Favorites"
)

urlpatterns = [
    path(r"users/<int:pk>/subscribe/", hello),
    path(r"recipes/<int:pk>/favorite/", favorite),
    path(r"recipes/<int:pk>/shopping_cart/",
         ShoppingListViewSet.as_view(
            {"get": "shopping_cart_add",
             "delete": "shopping_cart_del"})
         ),
    path("recipes/download_shopping_cart/",
         ShoppingListViewSet.as_view({"get": "download_shopping_list"})),
    path('', include(router.urls)),
]
