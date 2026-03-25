import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import requests
import pandas as pd

from config import GOOGLE_API_KEY, DATA_PATH


def fetch_businesses():
    print("📡 Fetching real business data...")

    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    params = {
        "location": "23.0225,72.5714",  # Ahmedabad
        "radius": 3000,
        "type": "restaurant",  # IMPORTANT: use type instead of vague keyword
        "key": GOOGLE_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    results = data.get("results", [])

    print(f"✅ Fetched {len(results)} businesses")

    return results


def process_data(results):
    print("⚙️ Processing data...")

    processed = []

    for place in results:
        processed.append({
            "name": place.get("name"),
            "rating": place.get("rating", 0),
            "reviews": place.get("user_ratings_total", 0),
            "price_level": place.get("price_level", 1),
            "lat": place["geometry"]["location"]["lat"],
            "lon": place["geometry"]["location"]["lng"],
            "place_id": place.get("place_id")
        })

    df = pd.DataFrame(processed)

    return df


def main():
    results = fetch_businesses()
    df = process_data(results)

    if df.empty:
        print("❌ No data fetched. Fix API or query.")
        return

    df.to_csv(DATA_PATH, index=False)
    print(f"💾 Saved to {DATA_PATH}")


if __name__ == "__main__":
    main()