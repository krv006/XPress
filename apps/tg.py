import requests

TOKEN = "7652120897:AAH6Ameln9LCyANjrT8BUwH0IccJapWYh1E"
CHAT_ID = -4913366579  # To‘g‘ri guruh ID
TEXT = "SALOM TEST"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
res = requests.post(url, data={"chat_id": CHAT_ID, "text": TEXT})

print(res.status_code, res.text)
