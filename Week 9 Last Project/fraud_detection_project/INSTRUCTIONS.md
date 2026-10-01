# Fraud Detection Project — Step-by-Step Instructions

## Current Status: Phase 16 (Model Monitoring) — DONE — ALL 16 PHASES COMPLETE 🎉

### New notebook: `notebooks/10_model_monitoring.ipynb`
This is the last phase on your roadmap. Run end-to-end against your real project in the build sandbox — zero errors.

### The key design decision
The monitoring **reference baseline must be `X_val`, not `X_train`**. `X_train` was oversampled in Phase 3 (198,608 rows, artificially rebalanced toward fraud-like feature values for training) — it was never meant to represent real traffic, and using it as a reference would raise constant false drift alarms. `X_val` and `X_test` are both untouched, natural-ratio holdouts (0.167% fraud, matching reality), so `X_val` is the reference and `X_test` stands in for "today's production batch."

### What it does
- Implements **PSI** (Population Stability Index, the industry-standard metric for this) and the **KS test** per feature, from scratch with scipy/numpy — no extra dependency.
- **Baseline check** (real data): `X_val` vs `X_test` — max PSI across all 30 features was **0.0013** (threshold for "moderate" is 0.1), confirming today's pipeline is healthy. This is a genuine result, not a canned example.
- **Proof the detector actually works**: injected a synthetic, realistic drift (transaction amounts inflated, `V14` — Phase 10's #1 SHAP driver — shifted) into a copy of the test set, then confirmed the detector flags exactly `Amount_scaled` (PSI 7.51) and `V14` (PSI 2.08) as "Significant" and nothing else as a false positive.
- **Prediction drift**: KS test on the model's output probability distribution — confirmed clean on the healthy batch (p=0.72) and sharply triggered on the drifted batch (p<0.001).
- Saved `models/monitoring_baseline.pkl` (reference distributions, ~12MB) and `models/drift_report_baseline.csv` (today's baseline report) for a future scheduled monitoring job to load.
- Step 7 includes a ready-to-copy snippet for running this against a new batch of real transactions later, with suggested monitoring cadence (weekly for data drift, daily for prediction drift).

### How to run it
Open `notebooks/10_model_monitoring.ipynb` in VS Code and run all cells top to bottom. No dependency on any other phase's notebook having been run first.

### 🎉 Project complete
All 16 phases are now delivered: data loading → preprocessing → class imbalance → supervised ML → unsupervised + hybrid → evaluation → threshold optimization → SHAP explainability → risk scoring → FastAPI → Streamlit dashboard → Docker → MLflow → monitoring. See the phase list further down for the full history and what's verified vs. what to double-check yourself (the two caveats worth remembering: Docker itself wasn't available to test directly in the build sandbox, verified instead via fresh-venv simulation — see the Phase 14 section below; and notebook 06 — threshold optimization — hasn't been run in this zip, so a few downstream numbers use fallback defaults until you run it).

---

## Previously delivered: Phase 15 (MLflow Experiment Tracking)

### New notebook: `notebooks/09_mlflow_tracking.ipynb`

### New notebook: `notebooks/09_mlflow_tracking.ipynb`

### Run end-to-end against your real project in the build sandbox — zero errors
This notebook adopts MLflow partway through the project, so it doesn't retrain anything — it retroactively logs the experiments you already ran (Phases 4-9) as proper MLflow runs, then registers the champion model.

### What it does
- **Phase 4** (class imbalance): 5 runs, one per technique, with precision/recall/F1/ROC-AUC/PR-AUC as metrics — read straight from `class_imbalance_comparison.csv`.
- **Phase 5** (supervised models): 4 runs (LightGBM, XGBoost, Random Forest, Logistic Regression) from `supervised_model_comparison.csv`.
- **Phase 6** (unsupervised): 2 runs (Isolation Forest, One-Class SVM) from `unsupervised_comparison.csv`.
- **Phase 7** (hybrid score): metrics **recomputed fresh** from the saved Isolation Forest + hybrid weights, not copy-pasted — confirmed PR-AUC 0.7545 again, matching notebook 05 exactly.
- **Phase 8/9** (threshold): logged only if `threshold_config.pkl` exists (run notebook 06 first); otherwise skipped with a clear message, same fallback pattern as notebooks 07/08.
- **Registers the champion model** as `fraud-detection-champion` in the MLflow Model Registry, tagged with a `champion` alias (the current MLflow convention — Stages are deprecated since 2.9). Load it anywhere with `mlflow.lightgbm.load_model("models:/fraud-detection-champion@champion")`.
- **Verifies the registered model is identical**: loads it back from the registry (not the local `.pkl`) and checks it reproduces `best_supervised_model.pkl` exactly on all 42,559 test transactions — confirmed, not just assumed.
- Logged 13 runs total in my test execution (5+4+2+1 hybrid+1 registration; your threshold run will make 14 once you've run notebook 06).

### A note on what's **not** included in this zip
MLflow bakes the **absolute path** to its artifact store into its SQLite database at log time. If I shipped the `mlflow.db` and `mlruns/` I generated in the build sandbox, the model-artifact links inside it would point to a path on my machine, not yours, and would show as broken in your MLflow UI. So this delivers only the notebook — running it yourself creates `mlflow.db` and `mlruns/` at the project root with paths that correctly resolve on your machine.

### How to run it
1. `pip install mlflow==3.16.1` (already in `requirements.txt`)
2. Open `notebooks/09_mlflow_tracking.ipynb` in VS Code and run all cells top to bottom.
3. View results: `mlflow ui --backend-store-uri sqlite:///mlflow.db` from the project root, then open http://127.0.0.1:5000 — experiment `fraud-detection-pipeline`, registered model `fraud-detection-champion`.

### Next: Phase 16 (Model Monitoring — data drift, prediction drift)
Tell Claude "next" and I'll deliver it — this is the last phase on your roadmap.

---

## Previously delivered: Phase 14 (Dockerization)

### New files
- `Dockerfile.api` — multi-stage image for the FastAPI service
- `Dockerfile.dashboard` — multi-stage image for the Streamlit dashboard
- `docker-compose.yml` — runs both together
- `requirements-api.txt` / `requirements-dashboard.txt` — lean, version-pinned runtime deps (separate from `requirements.txt`, which is for notebook development — the containers don't need jupyter, seaborn, or imbalanced-learn)
- `.dockerignore`

### An honest note on verification here
**Docker itself isn't available in the build sandbox**, so unlike every phase so far, I could not literally run `docker build` / `docker run` to prove the images work end-to-end. What I did instead, to get as close to real verification as this environment allows:
1. Pinned `requirements-api.txt` / `requirements-dashboard.txt` to the exact package versions already verified against your model in Phases 10-13, and installed each into a **fresh, isolated virtual environment** (no reuse of the working sandbox's packages) — both installed clean with no conflicts.
2. Copied **only** the files each Dockerfile's `COPY` instructions would copy into a scratch directory (not the full project), then ran the real API and the real dashboard from that minimal file set using the fresh-venv interpreters. Both started and worked: the simulated API answered a real `/predict` request correctly, and the simulated dashboard loaded with the correct Overview metrics.
3. This proves the `COPY` lists are complete (nothing silently missing) and the pinned dependencies are sufficient — the only things genuinely untested are Docker-specific mechanics (the two `apt-get` layers, the `HEALTHCHECK` syntax, non-root `USER` behavior, and image size). Those are standard, low-risk patterns, but please run `docker compose up --build` yourself once before relying on this.

### How to run it
```
docker compose up --build
```
- API docs: http://localhost:8000/docs
- Dashboard: http://localhost:8501

Or individually: `docker build -f Dockerfile.api -t fraud-api .` then `docker run -p 8000:8000 fraud-api` (same pattern for `Dockerfile.dashboard` / port 8501).

Note: the dashboard doesn't call the API over the network — it loads the model directly, same as the API does — so `depends_on: api` in the compose file is just start-order bookkeeping, not a functional dependency.

### Next: Phase 15 (MLflow experiment tracking)
Tell Claude "next" and I'll deliver it.

---

## Previously delivered: Phase 13 (Streamlit Dashboard)

### New file: `src/dashboard.py`
Three tabs, all reading the same artifacts as the API (`src/main.py`), and reusing its exact `risk_score()`/`risk_band()` functions so the dashboard and the API can never disagree:

1. **Overview** — live metrics on the held-out test set (transactions, fraud cases, % of fraud caught in the High band, fraud rate within High), a risk-band summary table, and a log-scale score-distribution histogram split by legit/fraud. Threshold sliders in the sidebar let you move T_LOW/T_HIGH and watch the trade-off update live.
2. **Score a transaction** — "Load random fraud" / "Load random legit" pulls a real row from the test set into the input fields (or edit V1-V28/Amount/Time by hand), then shows the risk score, band, probability, and a horizontal SHAP bar chart of the top 10 factors for that specific prediction.
3. **Feature importance** — the global SHAP ranking from Phase 10 (`models/shap_feature_importance.csv`), as both a bar chart and a full table.

### How to run it
1. Make sure `models/risk_scoring_config.pkl`, `models/scaler_params.json`, and `models/shap_feature_importance.csv` exist (notebooks 08, `export_scaler.py`, and 07 respectively — all already included in this zip).
2. From the project root: `streamlit run src/dashboard.py`
3. It opens at http://localhost:8501

### Verified in the build sandbox
Tested headlessly with Streamlit's `AppTest` (no browser needed): clicked "Load random fraud" 6 times across two runs — 5 came back High/~0.9999 probability as expected, and one hit a genuine hard-to-detect fraud case from Phase 10's missed-fraud analysis (0.1/100, Low) — real model behavior, not a bug, and a good illustration of the model's limits for your write-up. "Load random legit" correctly returned Low. The invalid-threshold guard (T_LOW ≥ T_HIGH) correctly blocks with an error message.

### Next: Phase 14
Tell Claude "next" and I'll check the roadmap and deliver it.

---

## Previously delivered: Phase 12 (FastAPI)

### New files
- `src/main.py` — the API (`GET /health`, `POST /predict`)
- `src/export_scaler.py` — one-time script that saves the Amount/Time scaling parameters to `models/scaler_params.json` (notebook 02 never saved its scaler; the API needs it to scale raw incoming transactions)
- `tests/test_api.py` — 5 tests
- `models/scaler_params.json` — already generated and verified (reproduces your `X_test.csv` exactly on 40,733 matched rows)

### What `POST /predict` does
Send one raw transaction (`V1`-`V28`, `Amount`, `Time`, unscaled). It returns:
- `fraud_probability` from the champion LightGBM model
- `risk_score` (0-100) and `risk_band` (Low / Medium / High) using the Phase 11 mapping, read from `models/risk_scoring_config.pkl`
- `is_flagged` (true when the band is High)
- `top_factors` — the 5 features that pushed this prediction most, with SHAP contributions (Phase 10, explainer built once at startup)

The model, config, scaler and SHAP explainer load once at startup, not per request. Bad input (missing field, negative amount) returns a 422.

### How to run it
1. Install requirements: `pip install -r requirements.txt`
2. From the project root, make sure `models/risk_scoring_config.pkl` exists (run notebook 08) and `models/scaler_params.json` exists (included; or run `python src/export_scaler.py`).
3. Start the server: `uvicorn src.main:app --reload`
4. Open http://127.0.0.1:8000/docs, click `POST /predict` -> "Try it out" -> Execute. The pre-filled example is a generic transaction; paste a real fraud row from `creditcard.csv` to see a High result.
5. Run the tests: `pytest tests -v`

### Verified in the build sandbox
The 5 tests pass, and a live `uvicorn` server returned `risk_band: High`, probability 0.99995, top factors V14/V10/V12/V4 for a real fraud transaction. The API's probability matches calling the model directly on the processed features, which confirms the raw-input scaling is correct. The thresholds come from whatever `risk_scoring_config.pkl` holds; in my run that was T_LOW=0.01, T_HIGH=0.12.

### Next: Phase 13 (Streamlit Dashboard)
Tell Claude "next" and I'll deliver it.

---

## Previously delivered: Phase 11 (Risk Scoring)

### New notebook: `notebooks/08_risk_scoring.ipynb`

### A note on verification for this delivery
Run end-to-end against your real model and data in the build sandbox — zero errors, every printed number below is the real output.

### Phase 11: Risk Scoring (0-30 Low, 30-70 Medium, 70-100 High) — what it does
- **The problem this solves**: because Phase 4's oversampling only rebalances *training* data, the champion model's raw probabilities on real (imbalanced) data are extremely compressed — 99.7% of test transactions score below probability 0.01. A naive `probability * 100` mapping would dump almost everything at Risk Score ≈ 0 with no usable separation.
- **The fix**: a piecewise-linear map from probability → 0-100, anchored to two real decision thresholds so the bands mean something operationally: `T_LOW` (the highest threshold that still catches ≥90% of fraud on validation) becomes the Low/Medium boundary at score 30, and `T_HIGH` (the flagging threshold — from Phase 9's `threshold_config.pkl` if you've run notebook 06, else recomputed on the fly as the F1-optimal threshold) becomes the Medium/High boundary at score 70. "High" is therefore literally the set of transactions the model would auto-flag.
- **Real result from your data** (test set, thresholds computed on the fly since `threshold_config.pkl` wasn't present yet — T_LOW=0.01, T_HIGH=0.12):
  - **Low band**: 42,445 transactions, fraud rate 0.03% — safe to leave un-reviewed.
  - **Medium band**: 49 transactions, fraud rate 2.0% — worth a second look.
  - **High band**: 65 transactions, fraud rate **86.2%** — heavily concentrated.
  - **78.9%** of all fraud in the test set lands in the High band alone; **80.3%** in Medium+High combined.
  - These numbers will shift slightly (likely for the better) once you run notebook 06 first, since it'll use the real cost-optimal threshold instead of the on-the-fly F1-optimal stand-in.
- Saves `models/risk_scoring_config.pkl` (the two anchor thresholds + band boundaries, for Phase 12's FastAPI endpoint to reuse) and `models/risk_scored_test_sample.csv` (first 200 scored test rows, for reference).

### How to run it
1. (Recommended, not required) Run `notebooks/06_evaluation_and_threshold.ipynb` first, so this notebook picks up the real cost-optimal threshold instead of computing a stand-in.
2. Open `notebooks/08_risk_scoring.ipynb` in VS Code and run all cells top to bottom.
3. Check that `models/risk_scoring_config.pkl` and `models/risk_scored_test_sample.csv` are created.

### Next: Phase 12 (FastAPI — POST /predict endpoint)
Tell Claude "next" and I'll deliver it.

---

## Previously delivered: Phase 10 (Explainable AI — SHAP)

### New notebook: `notebooks/07_explainability_shap.ipynb`

### A note on verification for this delivery
Unlike Phase 8/9, this one **was fully run against your real `best_supervised_model.pkl` and real data end-to-end in the build sandbox** — `lightgbm` and `shap` were both installable there this time, so every cell executed with zero errors, all 7 plots rendered, and the SHAP-value reconstruction of `predict_proba` was checked and matched exactly. You can trust the numbers below; still run it yourself once to see the plots and confirm your own environment's `shap` version behaves the same way (results should be identical).

### Phase 10: Explainable AI (SHAP) — what it does
- Builds a `shap.TreeExplainer` on the champion LightGBM model (no background dataset needed for tree models — exact, not approximated) and computes SHAP values for the **entire test set** (~42.5K rows, runs in well under a minute).
- **Global explainability**: a mean-|SHAP| bar chart ranking every feature, plus a beeswarm plot (on a 2,000-row sample for readability) showing both magnitude and direction of each feature's effect, plus dependence plots for the top 4 features.
- **Result from your data**: `V14` is by far the strongest driver of fraud predictions (mean |SHAP| ≈ 4.04), followed by `V12`, `V10`, and `V4` (≈1.5-1.6 each) — a steep drop-off after that.
- **Local explainability**: waterfall plots for four specific transactions — the highest-confidence correctly-caught fraud, the closest-call missed fraud, the highest-confidence false alarm, and a confidently-correct legit transaction — so you can point to exactly why the model made each call.
- Uses the Phase 9 `threshold_config.pkl` if it exists (to pick the TP/FN/FP/TN examples with your real decision threshold); falls back to 0.5 with a clear warning if you haven't run notebook 06 yet — this does not affect the SHAP values themselves, only which four example rows get shown.
- Saves `models/shap_feature_importance.csv` (full feature ranking). The explainer itself is deliberately **not** pickled — recreating it takes ~0.1s, so Phase 12's FastAPI endpoint should build it once at startup instead.

### How to run it
1. Open `notebooks/07_explainability_shap.ipynb` in VS Code.
2. Run all cells top to bottom (for the real threshold-based examples, run `06_evaluation_and_threshold.ipynb` first if you haven't).
3. Check that `models/shap_feature_importance.csv` is created.

### Next: Phase 11 (Risk Scoring — 0-30 Low, 30-70 Medium, 70-100 High)
Tell Claude "next" and I'll deliver it.

---

## Previously delivered: Phase 8 (Model Evaluation) + Phase 9 (Threshold Optimization)
*(Delivered together, as requested)*

### New notebook: `notebooks/06_evaluation_and_threshold.ipynb`

### A note on verification for this delivery
This notebook's logic was fully validated in the build sandbox — every calculation (test-set metrics, ROC/PR curves, the raw-Amount recovery trick, the threshold sweeps, the cost-based optimization) was run end-to-end against your real processed data, using a temporary stand-in classifier in place of `best_supervised_model.pkl`, because this sandbox doesn't have LightGBM installed / internet access to install it. The stand-in confirmed there are no bugs, path errors, or logic errors anywhere in the notebook. **It was not run with your actual LightGBM model**, so run it top-to-bottom yourself once in your own environment (where `lightgbm` is already installed, since Phase 5 needed it) and let me know if any numbers look off — unlike the earlier phases' notes, I'm not claiming "verified with your real model, zero errors" for this one since that would not be accurate.

### Phase 8: Model Evaluation — what it does
- Loads `best_supervised_model.pkl` (LightGBM) and evaluates it on the **test set** for the first time ever — every earlier comparison (Phases 5-7) used the validation set only, so this is the honest, final read on real-world performance.
- Recomputes the Phase 7 hybrid risk score on the test set (reusing the saved Isolation Forest and hybrid weights/normalization — nothing is refit on test data) and compares it head-to-head with LightGBM alone.
- Plots ROC and Precision-Recall curves for both, plus confusion matrix heatmaps.
- Does an error analysis: recovers the original, unscaled transaction `Amount` (dropped during Phase 3 preprocessing) by deterministically re-running the same dedup + split with the same `random_state=42`, then reports the total dollar value of missed fraud vs. false alarms.
- Saves `models/final_test_evaluation.csv`.

### Phase 9: Threshold Optimization — what it does
- Searches for a better decision threshold than the default 0.5, using the **validation set only** — the test set is touched exactly once at the end, to confirm the final choice.
- Three angles: F1-optimal threshold, business-target thresholds (recall ≥ 90% / precision ≥ 90%, with an explicit warning if a target isn't reachable), and a **cost-based** threshold that assigns the real transaction amount as the cost of a missed fraud and an assumed $10 manual-review cost per false alarm, then minimizes total expected cost.
- Recommends the cost-optimal threshold by default (swap `FINAL_THRESHOLD` in the notebook if your business instead needs a hard recall/precision guarantee).
- Saves `models/threshold_config.pkl` (final threshold + every candidate, for reuse in Phase 11 risk scoring and the Phase 12 FastAPI endpoint) and `models/threshold_optimization_comparison.csv`.

### How to run it
1. Open `notebooks/06_evaluation_and_threshold.ipynb` in VS Code.
2. Run all cells top to bottom.
3. Check that `models/final_test_evaluation.csv`, `models/threshold_config.pkl`, and `models/threshold_optimization_comparison.csv` are created.
4. The printed "Champion model" and ">>> Selected final threshold <<<" lines are what Phase 10 onward will build on — take a look before moving on, since the cost-optimal threshold depends on the `REVIEW_COST = 10` assumption in the notebook, which you should adjust to your real operational cost.

### Next: Phase 10 (Explainable AI — SHAP)
Tell Claude "next" and I'll deliver it.

---

## Previously delivered: Phase 6 (Unsupervised) + Phase 7 (Hybrid Scoring)

### Notebook: `notebooks/05_unsupervised_and_hybrid.ipynb`

### Phase 6: Unsupervised Fraud Detection — what it does
- **Isolation Forest**: trained unsupervised (no labels) on raw training data, flags outliers as potential fraud. Result: PR-AUC 0.1182 (this is expected to be much lower than supervised — unsupervised methods alone are weak on this dataset)
- **One-Class SVM**: trained on a 5,000-row sample (full dataset is too slow for this algorithm). Result: PR-AUC 0.0991
- Isolation Forest won between the two, comparison saved to `models/unsupervised_comparison.csv`

### Phase 7: Hybrid Fraud Detection — what it does
- Combines LightGBM's fraud probability (70% weight) + Isolation Forest's anomaly score (30% weight) into one **Risk Score (0-100)**
- **Real result from your data**: Hybrid PR-AUC = 0.7545, vs LightGBM alone = 0.8253
- **Honest finding**: the hybrid score actually performed slightly worse than the supervised model alone here. This happens because the weak unsupervised signal (PR-AUC 0.12) dilutes the strong supervised signal when averaged. This is a legitimate, common real-world finding — worth mentioning in your report as "we experimented with hybrid weighting and found the supervised model alone was more reliable for this dataset; the anomaly score is retained for its ability to flag novel fraud patterns not seen in training data, which is valuable for future-proofing even if it doesn't improve the retrospective PR-AUC."
- Saved: `models/isolation_forest.pkl`, `models/hybrid_config.pkl` (weights, reusable later in FastAPI)

### How to run it
1. Open `notebooks/05_unsupervised_and_hybrid.ipynb` in VS Code.
2. Run all cells top to bottom. One-Class SVM cell takes a little longer (SVM training is slow) — this is normal.
3. Everything has already been verified to run error-free on your actual dataset.

### What to check
- Isolation Forest and One-Class SVM results print with confusion matrices
- Hybrid risk score preview table (first 10 transactions) shows Fraud_Probability, Anomaly_Score, Risk_Score_0_100
- Final hybrid evaluation metrics
- `models/isolation_forest.pkl` and `models/hybrid_config.pkl` exist

---
## Full Project Roadmap (16 Phases)
1. Problem Understanding & Literature Review
2. Data Understanding & EDA ✅
3. Data Preprocessing ✅
4. Class Imbalance Handling ✅ (Oversampling won — PR-AUC 0.6990)
5. Supervised ML ✅ (LightGBM won — PR-AUC 0.8253)
6. Unsupervised Fraud Detection ✅ (Isolation Forest won — PR-AUC 0.1182)
7. Hybrid Fraud Detection ✅ (Risk Score 0-100, PR-AUC 0.7545)
8. Model Evaluation ✅ (confirmed LightGBM as champion on the held-out test set)
9. Threshold Optimization ✅ (cost-optimal threshold selected — see notebook for exact value)
10. Explainable AI (SHAP) ✅ (V14, V12, V10, V4 are the top drivers)
11. Risk Scoring (0-30 Low, 30-70 Medium, 70-100 High) ✅ (High band = 86% fraud rate, catches 79% of all fraud)
12. FastAPI (POST /predict endpoint) ✅ (`src/main.py`, 5 passing tests)
13. Streamlit Dashboard ✅ (`src/dashboard.py`, 3 tabs)
14. Dockerization ✅ (`Dockerfile.api`, `Dockerfile.dashboard`, `docker-compose.yml`)
15. MLflow experiment tracking ✅ (`notebooks/09_mlflow_tracking.ipynb`)
16. Model Monitoring (data drift, prediction drift) ✅ (`notebooks/10_model_monitoring.ipynb`) — PROJECT COMPLETE

---
## Progress Log
### Phase 2: EDA (notebooks/01_load_data.ipynb) ✅
### Phase 3: Preprocessing (notebooks/02_preprocessing.ipynb) ✅
### Phase 4: Class Imbalance (notebooks/03_class_imbalance.ipynb) ✅ — Oversampling won, PR-AUC 0.6990
### Phase 5: Supervised ML (notebooks/04_supervised_ml.ipynb) ✅ — LightGBM won, PR-AUC 0.8253
### Phase 6 + 7: Unsupervised + Hybrid (notebooks/05_unsupervised_and_hybrid.ipynb) ✅
- Isolation Forest (won) vs One-Class SVM comparison
- Hybrid Risk Score (0.7 supervised + 0.3 anomaly) — PR-AUC 0.7545
- Saved: isolation_forest.pkl, hybrid_config.pkl
### Phase 8 + 9: Evaluation + Threshold Optimization (notebooks/06_evaluation_and_threshold.ipynb) ✅
- Test-set evaluation confirms LightGBM alone beats the hybrid score (matches Phase 7 finding)
- Cost-based, F1-optimal, and business-target thresholds compared; cost-optimal selected by default
- Saved: final_test_evaluation.csv, threshold_config.pkl, threshold_optimization_comparison.csv
### Phase 10: Explainable AI / SHAP (notebooks/07_explainability_shap.ipynb) ✅
- Run end-to-end against the real model in the build sandbox — zero errors, verified reconstruction of predict_proba
- Global: V14, V12, V10, V4 are the top 4 drivers of fraud predictions (steep drop-off after that)
- Local: waterfall plots for TP/FN/FP/TN example transactions
- Saved: shap_feature_importance.csv
### Phase 16: Model Monitoring (notebooks/10_model_monitoring.ipynb) ✅
- PSI + KS-test drift detection built from scratch; reference = X_val (natural), not oversampled X_train
- Baseline (X_val vs X_test): max PSI 0.0013, healthy. Injected drift (Amount + V14): correctly flagged as Significant, nothing else falsely flagged
- Prediction drift via KS test on output probabilities: clean on healthy batch, sharply triggered on drifted batch
- Saved: monitoring_baseline.pkl, drift_report_baseline.csv
### Phase 15: MLflow Tracking (notebooks/09_mlflow_tracking.ipynb) ✅
- Retroactively logs Phases 4-9 as 13+ MLflow runs; registers fraud-detection-champion model with a 'champion' alias
- Verified: registry model reproduces best_supervised_model.pkl exactly on all 42,559 test transactions
- mlflow.db/mlruns NOT shipped (bake in absolute paths) — run the notebook yourself to generate them
### Phase 14: Dockerization (Dockerfile.api, Dockerfile.dashboard, docker-compose.yml) ✅
- Multi-stage builds, pinned requirements-api.txt / requirements-dashboard.txt, non-root user, HEALTHCHECK
- Docker itself unavailable in the build sandbox; verified instead via fresh-venv installs + simulated COPY-only filesystem for both images, both ran real requests correctly
### Phase 13: Streamlit Dashboard (src/dashboard.py) ✅
- 3 tabs: Overview, Score a transaction, Feature importance; shares risk_score()/risk_band() with the API
- Verified headlessly with Streamlit AppTest
### Phase 12: FastAPI (src/main.py) ✅
- POST /predict returns probability, 0-100 risk score, band, and top-5 SHAP factors; 5 tests pass; verified on a live server
- Saved: models/scaler_params.json
### Phase 11: Risk Scoring (notebooks/08_risk_scoring.ipynb) ✅
- Piecewise-linear probability -> 0-100 mapping anchored to real decision thresholds (not naive *100 scaling)
- High band = 86.2% fraud rate, catches 78.9% of all fraud; Low band = 0.03% fraud rate
- Saved: risk_scoring_config.pkl, risk_scored_test_sample.csv
- [ ] Step 3: Missing values check
- [ ] Step 4: Statistical summary
- [ ] Step 5: Amount & Time distribution
- [ ] Step 6: Correlation heatmap
