from rest_framework import serializers
from .models import Loan
from datetime import timedelta


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
        read_only_fields = ["id", "estimated_return", "borrow_date"]

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
        if validated_data["devolution_date"] > instance.estimated_return:
            instance.user.is_blocked = True
            instance.user.while_blocked = validated_data["devolution_date"] + timedelta(
                days=15
            )

            instance.user.save()
        instance.is_active = False
        instance.copy.quantity += 1
        instance.copy.save()
        instance.devolution_date = validated_data["devolution_date"]

        instance.save()

        return instance
