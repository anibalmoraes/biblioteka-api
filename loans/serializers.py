from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Loan
import ipdb


class LoanSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Loan:
        return Loan.objects.create(**validated_data)

    def update(self, instance: Loan, validated_data: dict) -> Loan:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "borrow_date",
            "estimated_return",
            "devolution_date",
            "is_active",
        ]
        read_only_fields = ["id", "estimated_return", "borrow_date"]
