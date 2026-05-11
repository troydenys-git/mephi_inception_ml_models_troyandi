import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "UCI_Credit_Card.csv"
MODEL_PATH = BASE_DIR / "models" / "model_v1.pkl"
ARTIFACTS_DIR = BASE_DIR / "data" / "artifacts"

data = pd.read_csv(DATA_PATH)

data = data.drop(columns=["ID"])

X = data.drop(columns=["default.payment.next.month"])
y = data["default.payment.next.month"]

FEATURES = X.columns.tolist()

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

pipeline.fit(X_train, y_train)

with open(MODEL_PATH, "wb") as f:
    pickle.dump(pipeline, f)
    
X_test.to_csv(ARTIFACTS_DIR / "X_test.csv", index=False)
y_test.to_csv(ARTIFACTS_DIR / "y_test.csv", index=False)

with open(ARTIFACTS_DIR / "features.json", "w") as f:
    json.dump(FEATURES, f)