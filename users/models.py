from django.db import models
from django.contrib.auth.models import AbstractUser


class UserType(models.TextChoices):
    DEFAULT = "student"
    COLLABORATOR = "collaborator"


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_type = models.CharField(
        max_length=20,
        default=UserType.DEFAULT,
        choices=UserType.choices
    )
    is_blocked = models.BooleanField(default=False)

    def __repr__(self) -> str:
        return f"<User ({self.first_name} - {self.user_type} - {self.is_blocked})>"
