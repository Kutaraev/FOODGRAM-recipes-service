from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (FavoriteViewSet, FollowersViewSet, IngredientViewSet,
                    RecipeViewSet, TagViewSet, subscribe)

router = SimpleRouter()
router.register('ingredients', IngredientViewSet)
router.register(r'recipes', RecipeViewSet, basename='recipes')
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
    path(r"users/<int:pk>/subscribe/", subscribe),
    path('', include(router.urls)),
]
