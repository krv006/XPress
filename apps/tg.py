import requests

from apps.models import TelegramConfig

config = TelegramConfig.objects.first()


TELEGRAM_TOKEN = str(config.bot_token).strip()  # "7652120897:AAH6Ameln9LCyANjrT8BUwH0IccJapWYh1E"
CHAT_ID = str(config.chat_id).strip()  # -4913366579


def send_to_telegram_order(order_data):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    if isinstance(order_data, dict):
        order = order_data.get("order", {})
        external_response = order_data.get("external_response", {})

        message = (
            f"🆕 New Order!\n\n"
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


def send_to_telegram_contact(quote_data, type_name="Quote Request"):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    message = (
        f"🆕 Contact request {type_name}!\n\n"
        f"📝 Title: {quote_data.get('title')}\n"
        f"📞 Phone: {quote_data.get('phone_number')}\n"
        f"📅 Created Date: {quote_data.get('created_at')}\n"
    )

    if quote_data.get("message"):
        message += f"💬 Message: {quote_data.get('message')}\n"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        res = requests.post(url, data=payload, timeout=10)
        res.raise_for_status()
    except Exception as e:
        print("❌ Telegram xato:", e)
