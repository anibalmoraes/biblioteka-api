# Generated by Django 4.1.6 on 2023-03-05 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=127, unique=True),
        ),
    ]
