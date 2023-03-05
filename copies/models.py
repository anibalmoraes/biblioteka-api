from django.db import models
from books.models import Book
from users.models import User

import datetime
from uuid import uuid4


class Copy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    quantity = models.PositiveSmallIntegerField()

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="copies")

    copies_users = models.ManyToManyField(User, through="Loan", related_name="copies_users")

    def __repr__(self) -> str:
        return f"<Copy ({self.quantity})>"


class Loan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    borrow_date = models.DateField(auto_now_add=True)
    estimated_return = models.DateField(default=borrow_date + datetime.timedelta(days=30))
    devolution_date = models.DateField(default=None)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return f"<Loan ({self.borrow_date})>"
