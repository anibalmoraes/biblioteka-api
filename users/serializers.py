from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User, UserType


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="User with this email already exists.",
            )
        ],
    )

    user_type = serializers.ChoiceField(
        choices=UserType.choices, default=UserType.DEFAULT
    )

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "user_type",
            "is_blocked",
            "is_superuser",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_superuser": {"read_only": True},
            "id": {"read_only": True},
        }

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)
