from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.models import ShippingPriceRequest, Order


class ShippingPriceSerializer(serializers.Serializer):
    pickup_zip = serializers.CharField()
    dropoff_zip = serializers.CharField()
    estimated_ship_date = serializers.DateField(format="%Y-%m-%d")  # 🔥
    vehicle_type = serializers.CharField()
    ship_via_id = serializers.CharField()
    vehicle_runs = serializers.CharField()


class ShippingPriceRequestSerializer(ModelSerializer):
    class Meta:
        model = ShippingPriceRequest
        fields = [
            "id",
            "pickup_zip",
            "dropoff_zip",
            "estimated_ship_date",
            "vehicle_type",
            "ship_via_id",
            "vehicle_runs",
            "created_at",
        ]


class OrderStep1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "pickup_zip",
            "dropoff_zip",
            "estimated_ship_date",
            "vehicle_type",
            "ship_via_id",
            "vehicle_runs",
            "calculated_price",
            "created_at",
        ]
        read_only_fields = ("id", "calculated_price", "created_at")


# Step2: update customer info (name, phone, email)
class OrderStep2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "name", "phone_number", "email"]
        read_only_fields = ("id",)
