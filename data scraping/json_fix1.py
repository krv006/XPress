import json

from apps.models.data_scrape import VehicleMake  # sizning model

with open("vehicle_makes.json", "r", encoding="utf-8") as f:
    data = json.load(f)

vehicle_makes = data.get("vehicle_makes", [])

for item in vehicle_makes:
    VehicleMake.objects.get_or_create(value=item["value"])

print("Ma'lumotlar bazaga yozildi ✅")
