import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data path
DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "real_business_data.csv")

# API KEY (IMPORTANT)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Ahmedabad coords
DEFAULT_LOCATION = {
    "lat": 23.0225,
    "lon": 72.5714
}

RADIUS = 3000  # meters

RANDOM_STATE = 42