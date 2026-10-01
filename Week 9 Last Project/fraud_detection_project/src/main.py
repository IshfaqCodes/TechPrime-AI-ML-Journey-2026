"""Phase 12: FastAPI service for real-time fraud scoring.

Run from the project root:
    uvicorn src.main:app --reload
Then open http://127.0.0.1:8000/docs for the interactive Swagger UI.
"""
import json
from contextlib import asynccontextmanager
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import shap
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parent.parent
MODELS = ROOT / "models"
FEATURES = [f"V{i}" for i in range(1, 29)] + ["Amount_scaled", "Time_scaled"]
TOP_N_FACTORS = 5

state = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load everything once at startup, not per request."""
    for name in ("best_supervised_model.pkl", "risk_scoring_config.pkl", "scaler_params.json"):
        if not (MODELS / name).exists():
            raise RuntimeError(
                f"models/{name} not found. Run notebook 08 (risk scoring) and "
                "`python src/export_scaler.py` first."
            )
    state["model"] = joblib.load(MODELS / "best_supervised_model.pkl")
    state["risk_cfg"] = joblib.load(MODELS / "risk_scoring_config.pkl")
    state["scaler"] = json.loads((MODELS / "scaler_params.json").read_text())
    state["explainer"] = shap.TreeExplainer(state["model"])  # ~0.1s to build
    yield
    state.clear()


app = FastAPI(
    title="Real-Time Credit Card Fraud Detection API",
    description="Scores a transaction with the champion LightGBM model, maps it to a "
    "0-100 risk score (Low/Medium/High) and explains it with SHAP.",
    version="1.0.0",
    lifespan=lifespan,
)


class Transaction(BaseModel):
    """One raw transaction, as in the original dataset (unscaled Amount and Time)."""

    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float = Field(..., ge=0, description="Transaction amount (raw, unscaled)")
    Time: float = Field(..., ge=0, description="Seconds elapsed since first transaction in the dataset")

    model_config = {
        "json_schema_extra": {
            "example": {
                "V1": -1.36, "V2": -0.07, "V3": 2.54, "V4": 1.38, "V5": -0.34,
                "V6": 0.46, "V7": 0.24, "V8": 0.10, "V9": 0.36, "V10": 0.09,
                "V11": -0.55, "V12": -0.62, "V13": -0.99, "V14": -0.31, "V15": 1.47,
                "V16": -0.47, "V17": 0.21, "V18": 0.03, "V19": 0.40, "V20": 0.25,
                "V21": -0.02, "V22": 0.28, "V23": -0.11, "V24": 0.07, "V25": 0.13,
                "V26": -0.19, "V27": 0.13, "V28": -0.02,
                "Amount": 149.62, "Time": 0,
            }
        }
    }


class Factor(BaseModel):
    feature: str
    value: float = Field(description="Feature value the model saw (Amount/Time are scaled)")
    shap_contribution: float = Field(description="Log-odds push: positive = toward fraud")


class Prediction(BaseModel):
    fraud_probability: float
    risk_score: float = Field(description="0-100")
    risk_band: str = Field(description="Low (<30), Medium (30-70) or High (>=70)")
    is_flagged: bool = Field(description="True when the risk band is High")
    top_factors: list[Factor]


def risk_score(p: float, t_low: float, t_high: float) -> float:
    """Same piecewise-linear mapping as notebook 08."""
    if p < t_low:
        return p / t_low * 30
    if p < t_high:
        return 30 + (p - t_low) / (t_high - t_low) * 40
    return 70 + min(max((p - t_high) / (1 - t_high), 0.0), 1.0) * 30


def risk_band(score: float) -> str:
    return "Low" if score < 30 else "Medium" if score < 70 else "High"


def to_features(tx: Transaction) -> pd.DataFrame:
    sc = state["scaler"]
    row = tx.model_dump()
    row["Amount_scaled"] = (row.pop("Amount") - sc["Amount"]["mean"]) / sc["Amount"]["scale"]
    row["Time_scaled"] = (row.pop("Time") - sc["Time"]["mean"]) / sc["Time"]["scale"]
    return pd.DataFrame([row])[FEATURES]


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model": type(state["model"]).__name__,
        "t_low": state["risk_cfg"]["t_low"],
        "t_high": state["risk_cfg"]["t_high"],
    }


@app.post("/predict", response_model=Prediction)
def predict(tx: Transaction):
    try:
        X = to_features(tx)
        proba = float(state["model"].predict_proba(X)[0, 1])
        cfg = state["risk_cfg"]
        score = float(np.clip(risk_score(proba, cfg["t_low"], cfg["t_high"]), 0, 100))
        band = risk_band(score)

        shap_row = state["explainer"].shap_values(X)[0]
        order = np.argsort(-np.abs(shap_row))[:TOP_N_FACTORS]
        factors = [
            Factor(feature=FEATURES[i], value=float(X.iloc[0, i]), shap_contribution=float(shap_row[i]))
            for i in order
        ]
    except Exception as exc:  # surface unexpected model errors as a clean 500
        raise HTTPException(status_code=500, detail=f"Prediction failed: {exc}")

    return Prediction(
        fraud_probability=proba,
        risk_score=round(score, 2),
        risk_band=band,
        is_flagged=band == "High",
        top_factors=factors,
    )
