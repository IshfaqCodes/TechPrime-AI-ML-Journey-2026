"""API tests. Run from the project root:  pytest tests -v"""
from pathlib import Path

import joblib
import pandas as pd
import pytest
from fastapi.testclient import TestClient

from src.main import app

ROOT = Path(__file__).resolve().parent.parent
RAW = pd.read_csv(ROOT / "data" / "creditcard.csv").drop_duplicates()
FEATURE_COLS = [f"V{i}" for i in range(1, 29)] + ["Amount", "Time"]


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:  # runs the lifespan (loads model at startup)
        yield c


def payload(row):
    return {c: float(row[c]) for c in FEATURE_COLS}


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_predict_matches_model_and_schema(client):
    """The API must give the same probability as calling the model directly on the
    processed features (proves the raw-input scaling is correct)."""
    X_test = pd.read_csv(ROOT / "data" / "processed" / "X_test.csv")
    model = joblib.load(ROOT / "models" / "best_supervised_model.pkl")
    vcols = [f"V{i}" for i in range(1, 29)]
    uniq = RAW[~RAW.duplicated(subset=vcols, keep=False)]
    merged = X_test.merge(uniq, on=vcols, how="inner").head(5)
    X_check = merged[list(X_test.columns)]
    expected = model.predict_proba(X_check)[:, 1]
    for (_, row), exp in zip(merged.iterrows(), expected):
        r = client.post("/predict", json=payload(row))
        assert r.status_code == 200
        body = r.json()
        assert body["fraud_probability"] == pytest.approx(exp, rel=1e-6, abs=1e-9)
        assert 0 <= body["risk_score"] <= 100
        assert body["risk_band"] in {"Low", "Medium", "High"}
        assert len(body["top_factors"]) == 5


def test_known_fraud_is_high_and_legit_is_low(client):
    X_test = pd.read_csv(ROOT / "data" / "processed" / "X_test.csv")
    y_test = pd.read_csv(ROOT / "data" / "processed" / "y_test.csv").squeeze()
    model = joblib.load(ROOT / "models" / "best_supervised_model.pkl")
    vcols = [f"V{i}" for i in range(1, 29)]
    uniq = RAW[~RAW.duplicated(subset=vcols, keep=False)]
    merged = X_test.merge(uniq, on=vcols, how="inner")
    merged["p"] = model.predict_proba(merged[X_test.columns])[:, 1]
    fraud = merged[merged.Class == 1].sort_values("p").iloc[-1]
    legit = merged[merged.Class == 0].sort_values("p").iloc[0]
    assert client.post("/predict", json=payload(fraud)).json()["risk_band"] == "High"
    assert client.post("/predict", json=payload(legit)).json()["risk_band"] == "Low"


def test_missing_field_rejected(client):
    r = client.post("/predict", json={"V1": 0.1})
    assert r.status_code == 422


def test_negative_amount_rejected(client):
    row = RAW.iloc[0]
    bad = payload(row)
    bad["Amount"] = -5
    assert client.post("/predict", json=bad).status_code == 422
