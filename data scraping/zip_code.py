import json
import time

import requests

BASE_URL = "https://back.usstartruckingllc.com/api/shipping/zip-codes/"
OUT_FILE = "zip_codes_full.json"
HEADERS = {"User-Agent": "kamron-fetch-script/1.0"}


def fetch_pages_batch(start_page, end_page):
    """start_page dan end_page gacha bo'lgan sahifalarni olish"""
    batch_results = []
    for page in range(start_page, end_page + 1):
        try:
            resp = requests.get(BASE_URL, params={"page": page}, headers=HEADERS, timeout=20)
            resp.raise_for_status()
            data = resp.json()
            batch_results.extend(data.get("results", []))
            print(f"[INFO] Page {page} fetched {len(data.get('results', []))} items")
        except Exception as e:
            print(f"[ERROR] Page {page} failed: {e}, retrying in 2s...")
            time.sleep(2)
            continue
    return batch_results


def main():
    # Dastlab total_pages ni olish
    r = requests.get(BASE_URL, headers=HEADERS, timeout=20)
    r.raise_for_status()
    data = r.json()
    total_pages = data.get("total_pages", 1)
    print(f"[INFO] Total pages: {total_pages}")

    all_results = []
    batch_size = 50  # har bir batchda 50 sahifa
    for start_page in range(1, total_pages + 1, batch_size):
        end_page = min(start_page + batch_size - 1, total_pages)
        print(f"[INFO] Fetching pages {start_page} to {end_page} ...")
        batch_results = fetch_pages_batch(start_page, end_page)
        all_results.extend(batch_results)
        time.sleep(0.2)  # kichik pauza serverni ortiqcha yuklamaslik uchun

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump({"zip_codes": all_results}, f, ensure_ascii=False, indent=2)

    print(f"[DONE] Saved {len(all_results)} items to {OUT_FILE}")


if __name__ == "__main__":
    main()
