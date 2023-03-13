from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Loan
from datetime import datetime, timedelta, date
import ipdb


class LoanSerializer(serializers.ModelSerializer):

    def create(self, validated_data: dict) -> Loan:
        if (date.today() + timedelta(days=15)).weekday() == 5:
            Loan["estimated_return"] == date.today() + timedelta(days=17)

        elif (date.today() + timedelta(days=15)).weekday() == 6:
            Loan["estimated_return"] == date.today() + timedelta(days=16)

        else:
            Loan["estimated_return"] == date.today() + timedelta(days=15)

        return Loan.objects.create(**validated_data)

    def update(self, instance: Loan, validated_data: dict) -> Loan:
        for key, value in validated_data.items():
            if key == "devolution_date" > key == "estimated_return":
                instance["is_active"] == False
            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = Loan
        fields = [
            "id",
            "borrow_date",
            "estimated_return",
            "devolution_date",
            "is_active",
        ]
        read_only_fields = ["id", "estimated_return", "borrow_date"]
