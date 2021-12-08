from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .filters import IngredientFilter, RecipeFilter
from .models import Favorite, Follow, Ingredient, Recipe, ShopList, Tag
from .pagination import CustomPagination
from .permissions import IsAuthenticatedPermission, RecipePermission
from .serializers import (FavoriteSerializer, FollowSerializer,
                          IngredientSerializer, MinRecipeSerializer,
                          RecipeSerializer, TagSerializer)
from .utils import from_cart_to_pdf


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (IngredientFilter,)
    search_fields = ('^name',)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [RecipePermission]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RecipeFilter

    @action(detail=True, methods=['get', 'delete'],
            permission_classes=[IsAuthenticated])
    def favorite(self, request, pk=None):
        """Добавить рецепт в избранное."""
        user = request.user
        if request.method == 'GET':
            if Favorite.objects.filter(user=user, recipe_id=pk).exists():
                return Response(
                    {'errors': 'Данный рецепт уже есть в избранном'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            Favorite.objects.create(user=user, recipe_id=pk)
            recipe = get_object_or_404(Recipe, id=pk)
            serializer = MinRecipeSerializer(recipe)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif request.method == 'DELETE':
            if Favorite.objects.filter(user=user, recipe_id=pk).exists():
                Favorite.objects.get(user=user, recipe_id=pk).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(
                {'errors': 'Данный рецепт уже удален из избранного'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return None

    @action(detail=True, methods=['get', 'delete'],
            permission_classes=[IsAuthenticated])
    def shopping_cart(self, request, pk=None):
        """Добавить рецепт в список покупок."""
        user = request.user
        if request.method == 'GET':
            if ShopList.objects.filter(user=user, recipe_id=pk).exists():
                return Response(
                    {'errors': 'Данный рецепт уже есть в списке покупок'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            ShopList.objects.create(user=user, recipe_id=pk)
            recipe = get_object_or_404(Recipe, id=pk)
            serializer = MinRecipeSerializer(recipe)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif request.method == 'DELETE':
            if ShopList.objects.filter(user=user, recipe_id=pk).exists():
                ShopList.objects.get(user=user, recipe_id=pk).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(
                {'errors': 'Данный рецепт уже удален из списка покупок'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return None

    @action(detail=False, methods=['get', 'delete'],
            permission_classes=[IsAuthenticated])
    def download_shopping_cart(self, request):
        user = self.request.user
        return from_cart_to_pdf(user)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class FollowersViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticatedPermission]

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(user=user)


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        user = self.request.user
        return Favorite.objects.filter(user=user)


@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def subscribe(request, pk):
    user = request.user
    if request.method == 'GET':
        if user.id == pk:
            return Response({
                'errors': 'Нельзя подписаться на самого себя'
            }, status=status.HTTP_400_BAD_REQUEST)
        if Follow.objects.filter(user=user, following_id=pk).exists():
            return Response({
                'errors': 'Вы уже подписаны на данного пользователя'
            }, status=status.HTTP_400_BAD_REQUEST)
        data = Follow.objects.get_or_create(
            user=user,
            following_id=pk
        )
        results = FollowSerializer(data[0]).data
        return Response(results)

    if request.method == 'DELETE':
        if user.id == pk:
            return Response({
                'errors': 'Нельзя отписаться от самого себя'
            }, status=status.HTTP_400_BAD_REQUEST)

        follow_to_delete = Follow.objects.filter(
            user=user,
            following_id=pk
        )
        if follow_to_delete.exists():
            follow_to_delete.delete()
            return Response({'message': "Вы отписались от пользователя!"})
        return Response({
            'errors': 'Вы не подписаны на данного пользователя'
        }, status=status.HTTP_400_BAD_REQUEST)
    return False
