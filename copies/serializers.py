from rest_framework import serializers

from .models import Copy, Loan


class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = ["id", "quantity"]
        read_only_fields = ["id"]

    def create(self, validated_data: dict) -> Copy:
        return Copy.objects.create(**validated_data)


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = [
            "id",
            "borrow_date",
            "estimated_return",
            "devolution_date"
        ]
        read_only_fields = ["id", "estimated_return"]

    def create(self, validated_data: dict) -> Loan:
        return Loan.objects.create(**validated_data)
