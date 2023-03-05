# Generated by Django 4.1.6 on 2023-03-05 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="genre",
            field=models.CharField(
                choices=[
                    ("Drama", "Drama"),
                    ("Romance", "Romance"),
                    ("Ficção", "Fiction"),
                    ("Não Ficção", "Non Fiction"),
                    ("Infantil", "Kids"),
                    ("Terror", "Horror"),
                    ("Suspense", "Triller"),
                    ("Ação e aventura", "Action Adventure"),
                ],
                max_length=30,
            ),
        ),
    ]
