from rest_framework import serializers

from .models import Book, Genre
from copies.models import Copy
from django.db.models import Sum


class BookSerializer(serializers.ModelSerializer):
    genre = serializers.ChoiceField(choices=Genre.choices)
    quantity = serializers.SerializerMethodField()

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
            "quantity",
        ]
        read_only_fields = ["created_at", "id"]

    def create(self, validated_data: dict) -> Book:
        existing_book = Book.objects.filter(
            title=validated_data.get("title"),
            author=validated_data.get("author")
        ).first()

        if existing_book:
            copy = Copy.objects.filter(book=existing_book).first()
            if copy:
                copy.quantity += 1
                copy.save()
            return existing_book
        
        new_book = Book.objects.create(**validated_data)
        Copy.objects.create(book=new_book, quantity=0)

        return new_book

    def update(self, instance: Book, validated_data: dict) -> Book:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    def get_quantity(self, obj: Book):
        copies = Copy.objects.filter(book=obj)
        return copies.aggregate(quantity=Sum("quantity"))["quantity"] or 0
