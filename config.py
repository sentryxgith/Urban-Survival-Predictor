import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# USE SYNTHETIC DATA ONLY
DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "business_data.csv")

RANDOM_STATE = 42
NUM_SAMPLES = 200