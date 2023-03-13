from rest_framework import serializers
from .models import Copy, Loan


class CopySerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()

    class Meta:
        model = Copy
        fields = ["id", "quantity", "book"]
        read_only_fields = ["id"]

    def create(self, validated_data: dict) -> Copy:
        copy = Copy.objects.filter(book=validated_data['book']).first()

        if copy:
            copy.quantity = copy.quantity + validated_data['quantity']
            copy.save()

            return copy
        
        return Copy.objects.create(**validated_data)

    def get_book(self, obj: Copy):
        return obj.book.title

    def update(self, instance: Copy, validated_data: dict) -> Copy:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance


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
