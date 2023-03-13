# Generated by Django 4.1.6 on 2023-03-05 13:06

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Copy",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("quantity", models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Loan",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("borrow_date", models.DateField(auto_now_add=True)),
                (
                    "estimated_return",
                    models.DateField(default=datetime.date(2023, 4, 4)),
                ),
                ("devolution_date", models.DateField(default=None)),
                (
                    "copy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="copies.copy"
                    ),
                ),
            ],
        ),
    ]