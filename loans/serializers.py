from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Loan
from datetime import datetime, timedelta, date
import ipdb
from users.models import User


class LoanSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)

    class Meta:
        model = Loan
        fields = [
            "id",
            "borrow_date",
            "estimated_return",
            "devolution_date",
            "is_active",
            "username",
        ]
        read_only_fields = ["id", "estimated_return"]

    def create(self, validated_data: dict) -> Loan:
        loan = Loan.objects.create(**validated_data)

        if loan.estimated_return.weekday() == 5:
            loan.estimated_return += timedelta(days=2)

        elif loan.estimated_return.weekday() == 6:
            loan.estimated_return += timedelta(days=1)

        loan.copy.quantity -= 1
        loan.copy.save()

        return loan

    def update(self, instance: Loan, validated_data: dict) -> Loan:
        for key, value in validated_data.items():
            if key == "devolution_date" > key == "estimated_return":
                instance["is_active"] = False
            setattr(instance, key, value)

        instance.save()

        return instance
