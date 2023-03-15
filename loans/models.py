from django.db import models
from uuid import uuid4
from datetime import datetime, timedelta, date
from users.models import User

# import datetime


class Loan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    borrow_date = models.DateField(auto_now_add=True)
    estimated_return = models.DateField(default=date.today() + timedelta(days=15))
    devolution_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(
        "users.user",
        on_delete=models.CASCADE,
        related_name="user_loans",
    )
    copy = models.ForeignKey(
        "copies.Copy",
        on_delete=models.CASCADE,
        related_name="copies_loans",
    )
    is_active = models.BooleanField(default=True)

    def __repr__(self) -> str:
        return f"<Loan ({self.user} - {self.copy} - {self.devolution_date})>"
