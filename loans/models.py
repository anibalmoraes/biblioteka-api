from django.db import models
from uuid import uuid4
import datetime


class Loan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    borrow_date = models.DateField(auto_now_add=True)
    estimated_return = models.DateField(default=datetime.date.today() + datetime.timedelta(days=30))
    devolution_date = models.DateField(null=True)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_loans",
    )
    copy = models.ForeignKey(
        "copies.Copy",
        on_delete=models.CASCADE,
        related_name="copy_loans",
    )
    is_active = models.BooleanField(default=True)

    def __repr__(self) -> str:
        return f"<Loan ({self.user} - {self.book_loans} - {self.devolution_date})>"
