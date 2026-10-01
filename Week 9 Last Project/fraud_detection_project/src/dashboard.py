"""Phase 13: Streamlit dashboard for the fraud detection system.

Run from the project root:
    streamlit run src/dashboard.py

Tabs:
  1. Overview        - how the risk bands perform on the held-out test set
  2. Score a transaction - pick or edit a transaction, see score, band and SHAP factors
  3. Feature importance  - global SHAP ranking from Phase 10

It loads the same artifacts as the API (src/main.py) and reuses its risk_score()
and risk_band() functions, so the dashboard and the API can never disagree.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shap
import streamlit as st

from src.landing import render_landing
from src.main import FEATURES, risk_band, risk_score

MODELS = ROOT / "models"
DATA = ROOT / "data" / "processed"
VCOLS = [f"V{i}" for i in range(1, 29)]

st.set_page_config(page_title="Fraud Detection Dashboard", page_icon="🛡️", layout="wide")


# --------------------------------------------------------------------------- loading
@st.cache_resource
def load_artifacts():
    needed = ["best_supervised_model.pkl", "risk_scoring_config.pkl", "scaler_params.json"]
    missing = [n for n in needed if not (MODELS / n).exists()]
    if missing:
        return None, missing
    model = joblib.load(MODELS / "best_supervised_model.pkl")
    return {
        "model": model,
        "cfg": joblib.load(MODELS / "risk_scoring_config.pkl"),
        "scaler": json.loads((MODELS / "scaler_params.json").read_text()),
        "explainer": shap.TreeExplainer(model),
    }, []


@st.cache_data
def load_test_data():
    return (
        pd.read_csv(DATA / "X_test.csv"),
        pd.read_csv(DATA / "y_test.csv").squeeze(),
    )


@st.cache_data
def test_probabilities(_model):
    X_test, _ = load_test_data()
    return _model.predict_proba(X_test)[:, 1]


def band_table(proba, y, t_low, t_high):
    scores = np.array([risk_score(p, t_low, t_high) for p in proba])
    bands = pd.Categorical(risk_band_array(scores), categories=["Low", "Medium", "High"], ordered=True)
    df = pd.DataFrame({"score": scores, "band": bands, "fraud": y.values})
    summary = df.groupby("band", observed=False).agg(
        transactions=("fraud", "count"), fraud_count=("fraud", "sum"), fraud_rate=("fraud", "mean")
    )
    total = max(int(summary["fraud_count"].sum()), 1)
    summary["share_of_all_fraud"] = summary["fraud_count"] / total
    return df, summary


def risk_band_array(scores):
    return [risk_band(s) for s in scores]


# --------------------------------------------------------------------------- page
art, missing = load_artifacts()

# Landing screen: shown first on every new session, until the user clicks "Open dashboard".
if art is not None and not st.session_state.get("entered"):
    render_landing(art["cfg"])  # calls st.stop() at the end

st.title("🛡️ Real-Time Credit Card Fraud Detection")

if art is None:
    st.error(
        f"Missing model files: {', '.join(missing)}. Run notebook 08 (risk scoring) and "
        "`python src/export_scaler.py`, then reload."
    )
    st.stop()

model, explainer, scaler = art["model"], art["explainer"], art["scaler"]

with st.sidebar:
    st.button("Back to home", on_click=lambda: st.session_state.update(entered=False))
    st.header("Risk thresholds")
    st.caption("Loaded from `models/risk_scoring_config.pkl`. Override to explore what-ifs.")
    t_low = st.number_input("T_LOW (Low → Medium)", 0.0001, 0.99, float(art["cfg"]["t_low"]), 0.005, format="%.4f")
    t_high = st.number_input("T_HIGH (Medium → High)", 0.0002, 0.999, float(art["cfg"]["t_high"]), 0.005, format="%.4f")
    if t_low >= t_high:
        st.error("T_LOW must be smaller than T_HIGH.")
        st.stop()
    st.markdown("**Bands:** Low 0-30 · Medium 30-70 · High 70-100")

tab_overview, tab_score, tab_importance = st.tabs(
    ["📊 Overview", "🔍 Score a transaction", "🧠 Feature importance"]
)

# --------------------------------------------------------------------------- tab 1
with tab_overview:
    X_test, y_test = load_test_data()
    proba = test_probabilities(model)
    df, summary = band_table(proba, y_test, t_low, t_high)

    total_fraud = int(y_test.sum())
    high = summary.loc["High"]
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Test transactions", f"{len(y_test):,}")
    c2.metric("Actual fraud cases", f"{total_fraud}")
    c3.metric("Fraud caught in High band", f"{high['share_of_all_fraud']:.1%}")
    c4.metric("Fraud rate in High band", f"{high['fraud_rate']:.1%}")

    left, right = st.columns(2)
    with left:
        st.subheader("Risk band summary")
        shown = summary.copy()
        shown["fraud_rate"] = shown["fraud_rate"].map("{:.2%}".format)
        shown["share_of_all_fraud"] = shown["share_of_all_fraud"].map("{:.1%}".format)
        shown.columns = ["Transactions", "Fraud cases", "Fraud rate in band", "Share of all fraud"]
        st.dataframe(shown, width='stretch')
        st.caption(
            "Low should hold almost no fraud; High should concentrate it. "
            "Change the thresholds in the sidebar to see the trade-off."
        )
    with right:
        st.subheader("Score distribution (log scale)")
        fig, ax = plt.subplots(figsize=(6, 3.5))
        ax.hist(df.loc[df.fraud == 0, "score"], bins=50, alpha=0.6, label="Legit", color="steelblue", log=True)
        ax.hist(df.loc[df.fraud == 1, "score"], bins=50, alpha=0.7, label="Fraud", color="crimson", log=True)
        ax.axvline(30, ls="--", color="grey")
        ax.axvline(70, ls="--", color="grey")
        ax.set_xlabel("Risk score")
        ax.set_ylabel("Transactions")
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

# --------------------------------------------------------------------------- tab 2
def load_sample(kind: str):
    """Fill the input widgets from a random test transaction (via session_state)."""
    X_test, y_test = load_test_data()
    pool = X_test[y_test.values == (1 if kind == "fraud" else 0)]
    row = pool.sample(1).iloc[0]
    for c in VCOLS:
        st.session_state[f"in_{c}"] = float(row[c])
    st.session_state["in_Amount"] = float(row["Amount_scaled"] * scaler["Amount"]["scale"] + scaler["Amount"]["mean"])
    st.session_state["in_Time"] = float(row["Time_scaled"] * scaler["Time"]["scale"] + scaler["Time"]["mean"])
    st.session_state["sample_kind"] = kind


for _k, _v in {"in_Amount": 50.0, "in_Time": 50000.0, **{f"in_{c}": 0.0 for c in VCOLS}}.items():
    st.session_state.setdefault(_k, _v)

with tab_score:
    st.write("Load a random real transaction from the held-out test set, or type your own values.")
    b1, b2, _ = st.columns([1, 1, 4])
    b1.button("Load random legit", on_click=load_sample, args=("legit",))
    b2.button("Load random fraud", on_click=load_sample, args=("fraud",))
    if "sample_kind" in st.session_state:
        st.caption(f"Loaded a random **{st.session_state['sample_kind']}** transaction from the test set.")

    a1, a2 = st.columns(2)
    amount = a1.number_input("Amount", min_value=0.0, key="in_Amount")
    time_s = a2.number_input("Time (seconds)", min_value=0.0, key="in_Time")

    with st.expander("PCA features V1-V28", expanded=False):
        cols = st.columns(4)
        vals = {}
        for i, c in enumerate(VCOLS):
            vals[c] = cols[i % 4].number_input(c, key=f"in_{c}", format="%.4f")

    row = dict(vals)
    row["Amount_scaled"] = (amount - scaler["Amount"]["mean"]) / scaler["Amount"]["scale"]
    row["Time_scaled"] = (time_s - scaler["Time"]["mean"]) / scaler["Time"]["scale"]
    X = pd.DataFrame([row])[FEATURES]

    p = float(model.predict_proba(X)[0, 1])
    score = float(np.clip(risk_score(p, t_low, t_high), 0, 100))
    band = risk_band(score)

    st.divider()
    m1, m2, m3 = st.columns(3)
    m1.metric("Risk score", f"{score:.1f} / 100")
    m2.metric("Risk band", band)
    m3.metric("Fraud probability", f"{p:.6f}")
    st.progress(min(score / 100, 1.0))
    {"Low": st.success, "Medium": st.warning, "High": st.error}[band](
        {
            "Low": "Low risk: no meaningful fraud signal.",
            "Medium": "Medium risk: worth a second look, not enough to auto-block.",
            "High": "High risk: this transaction would be flagged.",
        }[band]
    )

    st.subheader("Why this score? (top SHAP factors)")
    shap_row = explainer.shap_values(X)[0]
    order = np.argsort(-np.abs(shap_row))[:10][::-1]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.barh([FEATURES[i] for i in order], [shap_row[i] for i in order],
            color=["crimson" if shap_row[i] > 0 else "steelblue" for i in order])
    ax.axvline(0, color="black", lw=0.8)
    ax.set_xlabel("SHAP contribution (log-odds): red pushes toward fraud, blue toward legit")
    st.pyplot(fig)
    plt.close(fig)

# --------------------------------------------------------------------------- tab 3
with tab_importance:
    st.subheader("Global feature importance (mean |SHAP|, Phase 10)")
    imp_path = MODELS / "shap_feature_importance.csv"
    if imp_path.exists():
        imp = pd.read_csv(imp_path).head(15).set_index("feature")
        st.bar_chart(imp["mean_abs_shap"])
        st.dataframe(pd.read_csv(imp_path), width='stretch', hide_index=True)
    else:
        st.info("Run notebook 07 (SHAP) to generate `models/shap_feature_importance.csv`.")
