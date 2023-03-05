from django.db import models
from books.models import Book
from users.models import User


class Copy(models.Model):
    quantity = models.PositiveSmallIntegerField()

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="copies")

    copies_users = models.ManyToManyField(User, through="Loan", related_name="copies_users")

    def __repr__(self) -> str:
        return f"<Copy ({self.quantity})>"


class Loan(models.Model):
    borrow_date = models.DateField(auto_now_add=True)
    estimated_return = models.DateField(default=None)
    devolution_date = models.DateField(default=None)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return f"<Loan ({self.borrow_date})>"
