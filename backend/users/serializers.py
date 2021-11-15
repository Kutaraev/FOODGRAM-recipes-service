from djoser.serializers import UserSerializer

from users.models import User


class CustomUserSerializer(UserSerializer):
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


# Возможно не нужно, так как поля совпадают с CustomUserSerializer
class FollowUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('email',
                  'id',
                  'username',
                  'first_name',
                  'last_name',
                  'is_subscribed')
