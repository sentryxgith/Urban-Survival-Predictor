import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import requests
import pandas as pd
from textblob import TextBlob

from config import GOOGLE_API_KEY, DATA_PATH


def get_place_details(place_id):
    url = "https://maps.googleapis.com/maps/api/place/details/json"

    params = {
        "place_id": place_id,
        "fields": "name,reviews",
        "key": GOOGLE_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data.get("result", {})


def calculate_sentiment(reviews):
    if not reviews:
        return 0

    scores = []

    for review in reviews:
        text = review.get("text", "")
        if text:
            polarity = TextBlob(text).sentiment.polarity
            scores.append(polarity)

    if not scores:
        return 0

    return sum(scores) / len(scores)


def enrich_with_sentiment(df):
    print("🧠 Adding sentiment...")

    sentiments = []

    for idx, row in df.iterrows():
        place_id = row.get("place_id")

        if not place_id:
            sentiments.append(0)
            continue

        details = get_place_details(place_id)
        reviews = details.get("reviews", [])

        sentiment_score = calculate_sentiment(reviews)
        sentiments.append(sentiment_score)

        print(f"{row['name']} → {sentiment_score:.2f}")

    df["avg_sentiment"] = sentiments
    return df


def main():
    df = pd.read_csv(DATA_PATH)

    df = enrich_with_sentiment(df)

    df.to_csv(DATA_PATH, index=False)
    print("✅ Sentiment added and saved")


if __name__ == "__main__":
    main()