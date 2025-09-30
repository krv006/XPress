import json
import time

import requests

BASE_URL = "https://back.usstartruckingllc.com/api/shipping/vehicles/models/"
OUT_FILE = "vehicle_models.json"
HEADERS = {"User-Agent": "kamron-fetch-script/1.0"}


def fetch_all_vehicle_models():
    all_results = []
    page = 1

    while True:
        print(f"[INFO] Fetching page {page}...")
        try:
            resp = requests.get(BASE_URL, params={"page": page}, headers=HEADERS, timeout=20)
            resp.raise_for_status()
        except requests.RequestException as e:
            print(f"[ERROR] Page {page} failed: {e}. Retrying in 5s...")
            time.sleep(5)
            continue

        data = resp.json()
        results = data.get("results", [])
        all_results.extend(results)

        print(f"[INFO] Page {page} fetched {len(results)} items, total so far: {len(all_results)}")

        # Pagination: check if there is a next page
        links = data.get("links", {})
        if links.get("next"):
            page += 1
            time.sleep(0.1)  # small delay to be gentle to the API
        else:
            break

    return all_results


def main():
    vehicle_models = fetch_all_vehicle_models()
    final_json = {"vehicle_models": vehicle_models}
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(final_json, f, ensure_ascii=False, indent=2)
    print(f"[DONE] Saved {len(vehicle_models)} vehicle models to {OUT_FILE}")


if __name__ == "__main__":
    main()
