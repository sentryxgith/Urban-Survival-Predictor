import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
import numpy as np

from config import DATA_PATH, NUM_SAMPLES, RANDOM_STATE

np.random.seed(RANDOM_STATE)

def generate_data():
    print("⚙️ Generating synthetic business data...")

    data = {
        "name": [f"Business_{i}" for i in range(NUM_SAMPLES)],
        "rating": np.round(np.random.uniform(2.0, 5.0, NUM_SAMPLES), 1),
        "reviews": np.random.randint(5, 500, NUM_SAMPLES),
        "price_level": np.random.randint(1, 4, NUM_SAMPLES),
        "avg_sentiment": np.round(np.random.uniform(-1, 1, NUM_SAMPLES), 2),
        "competition": np.random.randint(1, 10, NUM_SAMPLES),
        "foot_traffic": np.random.randint(50, 500, NUM_SAMPLES),
    }

    df = pd.DataFrame(data)

    df.to_csv(DATA_PATH, index=False)
    print(f"✅ Data saved to {DATA_PATH}")


if __name__ == "__main__":
    generate_data()