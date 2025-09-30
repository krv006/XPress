import json

with open("vehicle_years.json", "r", encoding="utf-8") as f:
    data = json.load(f)

vehicle_makes = data.get("vehicle_years", [])

loaddata = []
for i, item in enumerate(vehicle_makes, start=1):
    loaddata.append({
        "model": "myapp.vehicleyear",
        "pk": i,
        "fields": {"value": item["value"]}
    })

with open("vehicle_years1.json", "w", encoding="utf-8") as f:
    json.dump(loaddata, f, ensure_ascii=False, indent=4)

print("Loaddata JSON tayyor ✅")
