from djoser.serializers import UserSerializer

from users.models import User


class CustomUserSerializer(UserSerializer):
    """Сериализатор для пользователей"""
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
            user.set_password(validated_data["password"])
            user.save()
            return user
