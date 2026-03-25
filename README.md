# 🏙️ Urban Business Survival Predictor

A machine learning-powered web application that predicts whether a business is likely to **survive or fail** based on key real-world factors like ratings, reviews, competition, sentiment, and foot traffic.

---

## 🚀 Features

* 📊 Predict business survival using ML (Random Forest)
* 🎛️ Interactive UI built with Streamlit
* 📈 Feature importance visualization
* 💡 Real-time input sliders for user simulation
* 🧠 Synthetic + optional real-world data pipeline
* 🧩 Modular code structure for scalability

---

## 🧠 How It Works

The model uses the following features:

* ⭐ Rating (1.0 – 5.0)
* 📝 Number of Reviews
* 💰 Price Level (1–3)
* 😊 Customer Sentiment (-1 to 1)
* 🏢 Competition (nearby businesses)
* 🚶 Foot Traffic

A **Random Forest Classifier** is trained on generated (or enriched) data to predict:

* ✅ SURVIVE
* ❌ FAIL

---

## 📁 Project Structure

```
Urban-Survival-Predictor/
│
├── app.py                     # Streamlit web app
├── config.py                  # Core configuration
├── configforealtime.py        # Config for real-time data (optional)
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
├── Figure_1.png               # Feature importance example
│
├── data/
│   └── raw/
│       ├── business_data.csv        # Synthetic dataset
│       └── real_business_data.csv   # Real-world data (optional)
│
├── src/
│   ├── data_generator.py      # Generates synthetic data
│   ├── data_collector.py      # (Optional) Fetch real business data
│   ├── sentiment_enricher.py  # Adds sentiment scores
│   └── survival_model.py      # Model training & prediction logic
```

---

## ⚙️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/sentryxgith/Urban-Survival-Predictor.git
cd Urban-Survival-Predictor
```

---

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 📊 Data Pipeline

### Option A (Current – Stable)

Uses synthetic data:

```bash
python src/data_generator.py
```

---

### Option B (Optional – Real Data)

```bash
python src/data_collector.py
python src/sentiment_enricher.py
```

⚠️ Requires API setup (can be skipped for now)

---

## 📈 Model Details

* Algorithm: Random Forest Classifier
* Evaluation Metrics:

  * Accuracy
  * Precision / Recall
  * Feature Importance

---

## 🧪 Example Output

* Prediction: **Likely to SURVIVE / FAIL**
* Confidence %
* Feature importance chart

---

## 🛠️ Tech Stack

* Python
* Pandas / NumPy
* Scikit-learn
* Streamlit
* Matplotlib

---

## 🚧 Future Improvements

* 🔗 Real-time Google Maps / Places API integration
* 🧠 Better sentiment analysis (transformer models)
* 📍 Location-based predictions
* ☁️ Cloud deployment with database support
* 📊 Dashboard analytics

---

## 🙌 Author

**Suraj Rajvanshi**

---

## ⭐ If you found this useful

Give it a star on GitHub — it helps a lot!
