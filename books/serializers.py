from rest_framework import serializers

from .models import Book, Genre
from copies.models import Copy
from django.db.models import Sum
from django.core.mail import send_mail
from django.conf import settings


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
            "following",
            "quantity",
        ]
        read_only_fields = ["created_at", "id", "following"]
        depth = 1

    def create(self, validated_data: dict) -> Book:
        existing_book = Book.objects.filter(
            title=validated_data.get("title"), author=validated_data.get("author")
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


class FollowingSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user_id = serializers.CharField(read_only=True)
    username = serializers.SerializerMethodField()
    book_id = serializers.CharField(read_only=True)

    def get_username(self, obj: Book):
        return obj.following.all().values("username")

    def create(self, validated_data):
        book = validated_data["book_id"]
        user = validated_data["user_id"]

        if book.following.filter(pk=user.id):
            book.following.remove(user)

        else:
            book.following.add(user)

            send_mail(
                subject="Disponibilidade do livro",
                message=f"Olá {user.first_name}! Você começou a seguir o livro {book.title} e no momento ele está {book.is_available}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )

        return book
