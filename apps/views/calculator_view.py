from datetime import date, datetime

import requests
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import Order
from apps.serializers import ShippingPriceSerializer, ShippingPriceRequestSerializer, OrderStep2Serializer, \
    OrderStep1Serializer


@extend_schema(tags=["Calculator"])
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


@extend_schema(tags=["Calculator"])
class TestShippingPriceAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ShippingPriceRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        payload = serializer.validated_data.copy()
        payload["estimated_ship_date"] = payload["estimated_ship_date"].strftime("%Y-%m-%d")

        external_url = "https://back.usstartruckingllc.com/api/shipping/price/"

        try:
            response = requests.post(external_url, json=payload)
            response.raise_for_status()
            data = response.json()

            shipping_request = serializer.save(
                calculated_price=list(data["data"].values())[0]  # 1130 ni olish
            )

            return Response(
                {
                    "request": ShippingPriceRequestSerializer(shipping_request).data,
                    "external_response": data,
                },
                status=response.status_code,
            )
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)


# class TestShippingPriceAPIView(APIView):
#     serializer_class = ShippingPriceRequestSerializer   # 🔥 qo‘shamiz
#     permission_classes = [AllowAny]
#
#     def post(self, request):
#         serializer = ShippingPriceRequestSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         # DB ga saqlash
#         shipping_request = serializer.save()
#
#         payload = serializer.validated_data.copy()
#         payload["estimated_ship_date"] = payload["estimated_ship_date"].strftime("%Y-%m-%d")
#
#         external_url = "https://back.usstartruckingllc.com/api/shipping/price/"
#
#         try:
#             response = requests.post(external_url, json=payload)
#             response.raise_for_status()
#             return Response(response.json(), status=response.status_code)
#         except requests.exceptions.RequestException as e:
#             return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)


EXTERNAL_PRICE_URL = "https://back.usstartruckingllc.com/api/shipping/price/"


@extend_schema(tags=["Orders"], request=OrderStep1Serializer, responses={201: OrderStep1Serializer})
class OrderStep1CreateAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = OrderStep1Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 1) saqlaymiz (customer maydonlari bo'sh)
        order = serializer.save()

        # 2) tashqi API ga yuboramiz (date string format)
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

            # 3) price topilsa saqlaymiz (safest extraction)
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
            # tashqi API xatolik bo'lsa ham order DBda saqlanib qoladi
            out = OrderStep1Serializer(order).data
            return Response({"order": out, "external_error": str(e)}, status=status.HTTP_201_CREATED)


@extend_schema(tags=["Orders"], request=OrderStep2Serializer, responses={200: OrderStep2Serializer})
class OrderStep2UpdateAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"detail": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderStep2Serializer(order, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
