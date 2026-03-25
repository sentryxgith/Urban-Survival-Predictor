import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from config import DATA_PATH, RANDOM_STATE


# ----------------------------
# Load Data
# ----------------------------
def load_data():
    df = pd.read_csv(DATA_PATH)
    return df


# ----------------------------
# Create Target (SMART LOGIC)
# ----------------------------
def create_target(df):
    df["target"] = (
        (df["rating"] > 3.5) &
        (df["reviews"] > 50) &
        (df["avg_sentiment"] > 0) &
        (df["competition"] < 7) &
        (df["foot_traffic"] > 100)
    ).astype(int)

    return df


# ----------------------------
# Feature Engineering
# ----------------------------
def engineer_features(df):
    df["review_density"] = df["reviews"] / (df["competition"] + 1)
    df["rating_sentiment"] = df["rating"] * df["avg_sentiment"]
    return df


# ----------------------------
# Train Model
# ----------------------------
def train_model():
    df = load_data()
    df = create_target(df)
    df = engineer_features(df)

    features = [
        "rating",
        "reviews",
        "price_level",
        "avg_sentiment",
        "competition",
        "foot_traffic",
        "review_density",
        "rating_sentiment"
    ]

    X = df[features]
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=RANDOM_STATE
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=RANDOM_STATE
    )

    model.fit(X_train, y_train)

    return model, features


# ----------------------------
# Explain Prediction
# ----------------------------
def explain_prediction(input_df):
    explanations = []

    if input_df["competition"].values[0] > 7:
        explanations.append("⚠️ High competition is hurting survival chances")

    if input_df["avg_sentiment"].values[0] > 0.5:
        explanations.append("✅ Strong customer sentiment is helping")

    if input_df["foot_traffic"].values[0] > 200:
        explanations.append("✅ High foot traffic increases survival chances")

    if input_df["rating"].values[0] < 3:
        explanations.append("⚠️ Low rating is a risk factor")

    return explanations