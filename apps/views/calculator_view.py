import requests
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.serializers import OrderStep1Serializer

EXTERNAL_PRICE_URL = "https://back.usstartruckingllc.com/api/shipping/price/"

TELEGRAM_TOKEN = "7652120897:AAH6Ameln9LCyANjrT8BUwH0IccJapWYh1E"
CHAT_ID = -4913366579


def send_to_telegram(order_data):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    if isinstance(order_data, dict):
        order = order_data.get("order", {})
        external_response = order_data.get("external_response", {})

        message = (
            f"🆕 Yangi Order!\n\n"
            f"📦 Order ID: {order.get('id')}\n"
            f"📍 Pickup ZIP: {order.get('pickup_zip')}\n"
            f"📍 Dropoff ZIP: {order.get('dropoff_zip')}\n"
            f"📅 Ship Date: {order.get('estimated_ship_date')}\n"
            f"🚗 Vehicle Type: {order.get('vehicle_type')}\n"
            f"🚚 Ship Via ID: {order.get('ship_via_id')}\n"
            f"🔄 Vehicle Runs: {order.get('vehicle_runs')}\n"
            f"💰 Calculated Price: {order.get('calculated_price')}\n"
            f"👤 Name: {order.get('name')}\n"
            f"📞 Phone: {order.get('phone_number')}\n"
            f"✉️ Email: {order.get('email')}\n"
        )

        if external_response.get("data"):
            prices = ", ".join([f"{k}: {v}" for k, v in external_response["data"].items()])
            message += f"\n💹 External Price: {prices}"

    else:
        message = str(order_data)

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        res = requests.post(url, data=payload, timeout=10)
        res.raise_for_status()
    except Exception as e:
        print("❌ Telegram xato:", e)


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

            send_to_telegram({
                "message": "🆕 Yangi Order!",
                "order": out,
                "external_response": data
            })

            return Response({"order": out, "external_response": data}, status=status.HTTP_201_CREATED)

        except requests.exceptions.RequestException as e:
            out = OrderStep1Serializer(order).data

            send_to_telegram(f"❌ External API error: {str(e)}")

            return Response({"order": out, "external_error": str(e)}, status=status.HTTP_201_CREATED)
