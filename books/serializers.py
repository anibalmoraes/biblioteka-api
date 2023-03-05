from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Book, Genre


class BookSerializer(serializers.ModelSerializer):
    genre = serializers.ChoiceField(choices=Genre.choices)

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "description",
            "pages",
            "genre",
            "published_at",
            "is_available",
            "created_at",
        ]
        extra_kwargs = {
            "created_at": {"read_only": True},
            "id": {"read_only": True},
        }

    def create(self, validated_data: dict) -> Book:
        return Book.objects.create(**validated_data)
