from django.db import models
from users.models import User
from uuid import uuid4


class Available(models.TextChoices):
    DEFAULT = "Disponível"
    INDISPONIVEL = "Indisponível"


class Genre(models.TextChoices):
    DRAMA = ("Drama",)
    ROMANCE = ("Romance",)
    FICTION = ("Ficção",)
    NON_FICTION = ("Não Ficção",)
    KIDS = ("Infantil",)
    HORROR = ("Terror",)
    TRILLER = ("Suspense",)
    ACTION_ADVENTURE = "Ação e aventura"


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=150)
    pages = models.PositiveSmallIntegerField()
    is_available = models.CharField(
        max_length=20, choices=Available.choices, default=Available.DEFAULT
    )
    genre = models.CharField(max_length=30, choices=Genre.choices)
    description = models.TextField()
    published_at = models.PositiveSmallIntegerField()
    author = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    following = models.ManyToManyField(User, related_name="followers")

    def __repr__(self) -> str:
        return f"<Book ({self.title} - {self.author} - {self.genre})>"
