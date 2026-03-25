import streamlit as st

# MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="Urban Survival Predictor", layout="centered")

import pandas as pd
import matplotlib.pyplot as plt

from src.survival_model import train_model, explain_prediction
from config import RANDOM_STATE


# ----------------------------
# Train Model (Cached)
# ----------------------------
@st.cache_resource
def get_model():
    model, features = train_model()
    return model, features


model, features = get_model()


# ----------------------------
# UI HEADER
# ----------------------------
st.title("🏙️ Urban Business Survival Predictor")
st.markdown("Predict whether a business will survive based on key factors.")


# ----------------------------
# USER INPUTS
# ----------------------------
rating = st.slider("Rating", 1.0, 5.0, 3.5)
reviews = st.number_input("Number of Reviews", 0, 1000, 100)
price_level = st.selectbox("Price Level", [1, 2, 3, 4])
sentiment = st.slider("Customer Sentiment", -1.0, 1.0, 0.0)
competition = st.slider("Competition (nearby businesses)", 1, 10, 5)
foot_traffic = st.slider("Foot Traffic", 0, 500, 200)


# ----------------------------
# PREDICT BUTTON
# ----------------------------
if st.button("Predict"):

    # Create input dataframe
    input_data = pd.DataFrame([{
        "rating": rating,
        "reviews": reviews,
        "price_level": price_level,
        "avg_sentiment": sentiment,
        "competition": competition,
        "foot_traffic": foot_traffic
    }])

    # Feature Engineering (MUST MATCH MODEL)
    input_data["review_density"] = input_data["reviews"] / (input_data["competition"] + 1)
    input_data["rating_sentiment"] = input_data["rating"] * input_data["avg_sentiment"]

    # Reorder columns
    input_data = input_data[features]

    # Prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][prediction]

    # ----------------------------
    # RESULT DISPLAY
    # ----------------------------
    st.subheader("Prediction Result")

    if prediction == 1:
        st.success(f"✅ Likely to SURVIVE ({probability*100:.2f}%)")
    else:
        st.error(f"❌ Likely to FAIL ({probability*100:.2f}%)")

    # ----------------------------
    # EXPLANATION (NEW 🔥)
    # ----------------------------
    st.subheader("Why this prediction?")

    explanations = explain_prediction(input_data)

    if explanations:
        for exp in explanations:
            st.write(exp)
    else:
        st.write("No strong factors detected.")


    # ----------------------------
    # FEATURE IMPORTANCE
    # ----------------------------
    st.subheader("Feature Importance")

    importances = model.feature_importances_

    fig, ax = plt.subplots()
    ax.barh(features, importances)
    ax.set_title("Feature Importance")

    st.pyplot(fig)