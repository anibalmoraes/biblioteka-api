from rest_framework import serializers

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
        read_only_fields = ["created_at", "id"]

    def create(self, validated_data: dict) -> Book:
        return Book.objects.create(**validated_data)

    def update(self, instance: Book, validated_data: dict) -> Book:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
