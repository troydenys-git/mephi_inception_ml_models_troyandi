import json
import pickle
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# пути
MODEL_PATH = BASE_DIR / "models" / "model_v1.pkl"
FEATURES_PATH = BASE_DIR / "data" / "artifacts" / "features.json"

# загрузка модели
def load_model():
    with open(MODEL_PATH, 'rb') as f:
        return pickle.load(f)


model = load_model()

# загрузка признаков
with open(FEATURES_PATH) as f:
    FEATURES = json.load(f)


# preprocessing
def preprocess_input(data):
    return np.array([[data[f] for f in FEATURES]])


# inference
def predict(data):
    features = preprocess_input(data)

    pred = model.predict(features)
    proba = model.predict_proba(features)[0][1]

    return {
        "prediction": int(pred[0]),
        "probability": float(proba),
        "model_version": "v1"
    }