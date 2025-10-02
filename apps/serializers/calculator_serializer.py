from rest_framework import serializers

from apps.models import Order


class OrderStep1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ("id", "calculated_price", "created_at")
