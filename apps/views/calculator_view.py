import requests
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.serializers import OrderStep1Serializer

EXTERNAL_PRICE_URL = "https://back.usstartruckingllc.com/api/shipping/price/"


@extend_schema(tags=["Orders"], request=OrderStep1Serializer, responses={201: OrderStep1Serializer})
class OrderStep1CreateAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = OrderStep1Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        payload = {
            "pickup_zip": order.pickup_zip,
            "dropoff_zip": order.dropoff_zip,
            "estimated_ship_date": order.estimated_ship_date.strftime("%Y-%m-%d"),
            "vehicle_type": order.vehicle_type,
            "ship_via_id": order.ship_via_id,
            "vehicle_runs": order.vehicle_runs,
        }

        try:
            resp = requests.post(EXTERNAL_PRICE_URL, json=payload, timeout=15)
            resp.raise_for_status()
            data = resp.json()

            price = None
            if isinstance(data, dict) and "data" in data and isinstance(data["data"], dict):
                vals = list(data["data"].values())
                if vals:
                    price = vals[0]

            if price is not None:
                order.calculated_price = price
                order.save()

            out = OrderStep1Serializer(order).data
            return Response({"order": out, "external_response": data}, status=status.HTTP_201_CREATED)

        except requests.exceptions.RequestException as e:
            out = OrderStep1Serializer(order).data
            return Response({"order": out, "external_error": str(e)}, status=status.HTTP_201_CREATED)
