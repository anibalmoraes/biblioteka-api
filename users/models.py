from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


class UserType(models.TextChoices):
    DEFAULT = "Estudante"
    COLLABORATOR = "Colaborador"


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=127, unique=True)
    user_type = models.CharField(
        max_length=20, default=UserType.DEFAULT, choices=UserType.choices
    )
    is_active = models.BooleanField(default=True)
    is_blocked = models.BooleanField(default=False)
    while_blocked = models.DateField(null=True)

    def __repr__(self) -> str:
        return f"<User ({self.first_name} - {self.user_type} - {self.is_blocked})>"
