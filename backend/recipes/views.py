
from io import BytesIO

from django.http import HttpResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from rest_framework.decorators import action

from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from .filters import RecipeFilter

from users.models import User

from rest_framework.permissions import IsAuthenticated

from .models import Amount, Favorite, Follow, Ingredient, Recipe, Tag, ShopList
from .pagination import CustomPagination
from .permissions import (IngredientPermission, IsAuthenticatedPermission,
                          RecipePermission)
from .serializers import (AmountSerializer, FavoriteSerializer,
                          FollowSerializer, IngredientSerializer,
                          RecipeSerializer, ShoppingSerializer, TagSerializer, MinRecipeSerializer)

from .utils import from_cart_to_pdf


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    # permission_classes = [IngredientPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', ]


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
        recipe = Recipe(id=pk)
        if request.method == 'GET':
            if Favorite.objects.filter(user=user, recipe=recipe).exists():
                return Response({'errors' : 'Данный рецепт уже есть в избранном'}, status=status.HTTP_400_BAD_REQUEST)
            Favorite.objects.create(user=user, recipe=recipe)
            serializer = MinRecipeSerializer(recipe)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif request.method == 'DELETE':
            if Favorite.objects.filter(user=user, recipe=recipe).exists():
                Favorite.objects.get(user=user, recipe=recipe).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response({'errors' : 'Данный рецепт уже удален из избранного'}, status=status.HTTP_400_BAD_REQUEST)
        return None

    @action(detail=True, methods=['get', 'delete'],
            permission_classes=[IsAuthenticated])
    def shopping_cart(self, request, pk=None):
        """Добавить рецепт в список покупок."""
        user = request.user
        recipe = Recipe(id=pk)
        if request.method == 'GET':
            if ShopList.objects.filter(user=user, recipe=recipe).exists():
                return Response({'errors' : 'Данный рецепт уже есть в списке покупок'}, status=status.HTTP_400_BAD_REQUEST)
            ShopList.objects.create(user=user, recipe=recipe)
            serializer = MinRecipeSerializer(recipe)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif request.method == 'DELETE':
            if ShopList.objects.filter(user=user, recipe=recipe).exists():
                ShopList.objects.get(user=user, recipe=recipe).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response({'errors' : 'Данный рецепт уже удален из списка покупок'}, status=status.HTTP_400_BAD_REQUEST)
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
def subscribe(request, pk):
    user = request.user
    following = User(id=pk)
    if request.method == 'GET':
        if user == following:
            return Response({
                'errors': 'Нельзя подписаться на самого себя'
            }, status=status.HTTP_400_BAD_REQUEST)
        if Follow.objects.filter(user=user, following=following).exists():
            return Response({
                'errors': 'Вы уже подписаны на данного пользователя'
            }, status=status.HTTP_400_BAD_REQUEST)
        data = Follow.objects.get_or_create(
            user=user,
            following=following
        )
        results = FollowSerializer(data[0]).data
        return Response(results)

    if request.method == 'DELETE':
        if user == following:
            return Response({
                'errors': 'Нельзя отписаться от самого себя'
            }, status=status.HTTP_400_BAD_REQUEST)

        follow_to_delete = Follow.objects.filter(
            user=user,
            following=following
        )
        if follow_to_delete.exists():
            follow_to_delete.delete()
            return Response({'message': "Вы отписались от пользователя!"})
        return Response({
            'errors': 'Вы не подписаны на данного пользователя'
        }, status=status.HTTP_400_BAD_REQUEST)
    return False

