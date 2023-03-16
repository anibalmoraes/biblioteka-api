from django.db import models
from books.models import Book
from users.models import User
from loans.models import Loan
from uuid import uuid4


class Copy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    quantity = models.PositiveSmallIntegerField()

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="copies")

    # copies_users = models.ManyToManyField(
    #     User, through=Loan, related_name="copies_users"
    # )

    def __repr__(self) -> str:
        return f"<Copy ({self.quantity})>"
