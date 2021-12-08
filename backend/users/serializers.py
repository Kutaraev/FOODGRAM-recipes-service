from djoser.serializers import UserSerializer
from rest_framework import serializers

from recipes.models import Follow
from users.models import User


class CustomUserSerializer(UserSerializer):
    """Сериализатор для пользователей"""
    is_subscribed = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('email',
                  'id',
                  'username',
                  'first_name',
                  'last_name',
                  'is_subscribed')

        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User(**validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user

        def get_is_subscribed(self, obj):
            """Статус подписки пользователя"""
            user = self.context.get('request').user
            if user.is_anonymous:
                return False
            return Follow.objects.filter(user=user, following=obj.id).exists()
