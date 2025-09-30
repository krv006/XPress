import json
import time

import requests

BASE_URL = "https://back.usstartruckingllc.com/api/shipping/vehicles/make/"
OUT_FILE = "vehicle_makes.json"
HEADERS = {"User-Agent": "kamron-fetch-script/1.0"}


def fetch_all_vehicle_makes():
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
    vehicle_makes = fetch_all_vehicle_makes()
    final_json = {"vehicle_makes": vehicle_makes}
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(final_json, f, ensure_ascii=False, indent=2)
    print(f"[DONE] Saved {len(vehicle_makes)} vehicle makes to {OUT_FILE}")


if __name__ == "__main__":
    main()
