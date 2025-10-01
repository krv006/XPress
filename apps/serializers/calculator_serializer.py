from rest_framework import serializers

class ShippingPriceSerializer(serializers.Serializer):
    pickup_zip = serializers.CharField()
    dropoff_zip = serializers.CharField()
    estimated_ship_date = serializers.DateField(format="%Y-%m-%d")  # 🔥
    vehicle_type = serializers.CharField()
    ship_via_id = serializers.CharField()
    vehicle_runs = serializers.CharField()
