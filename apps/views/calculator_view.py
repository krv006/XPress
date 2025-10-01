import requests
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.serializers import ShippingPriceSerializer

from datetime import date, datetime

class ShippingPriceAPIView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request=ShippingPriceSerializer,
        responses={200: dict}
    )
    def post(self, request):
        serializer = ShippingPriceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        external_url = "https://back.usstartruckingllc.com/api/shipping/price/"
        payload = serializer.validated_data.copy()

        if isinstance(payload.get("estimated_ship_date"), (date, datetime)):
            payload["estimated_ship_date"] = payload["estimated_ship_date"].strftime("%Y-%m-%d")

        try:
            response = requests.post(external_url, json=payload)
            response.raise_for_status()
            return Response(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)