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
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "user_type",
            "is_active",
            "is_blocked",
            "is_superuser",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_superuser": {"read_only": True},
            "id": {"read_only": True},
        }

    def create(self, validated_data: dict) -> User:
        if validated_data["user_type"] == "Colaborador":
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

            if key == "password":
                instance.set_password(value)

        instance.save()

        return instance
