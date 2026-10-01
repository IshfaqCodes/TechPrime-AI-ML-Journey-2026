"""Export the Amount/Time scaling parameters used in Phase 3 (notebook 02).

Notebook 02 fit StandardScaler on the de-duplicated full dataset but never saved
it. The API needs the same mean/std to scale raw Amount and Time from incoming
transactions, so this script recreates them and verifies against X_test.csv.

Run once from the project root:  python src/export_scaler.py
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

df = pd.read_csv(ROOT / "data" / "creditcard.csv").drop_duplicates()

params = {
    col: {"mean": float(df[col].mean()), "scale": float(df[col].std(ddof=0))}
    for col in ("Amount", "Time")
}

# Verify: rescaling the raw columns must reproduce the saved test features.
X_test = pd.read_csv(ROOT / "data" / "processed" / "X_test.csv")
scaled_amount = (df["Amount"] - params["Amount"]["mean"]) / params["Amount"]["scale"]
scaled_time = (df["Time"] - params["Time"]["mean"]) / params["Time"]["scale"]
# Exact check against X_test rows. Match on V1..V28, keeping only keys that are
# unique in the raw data (a few transactions share identical V values).
vcols = [f"V{i}" for i in range(1, 29)]
unique_raw = df.assign(Amount_chk=scaled_amount, Time_chk=scaled_time)
unique_raw = unique_raw[~unique_raw.duplicated(subset=vcols, keep=False)]
merged = X_test.merge(unique_raw, on=vcols, how="inner")
assert len(merged) > 1000, "too few uniquely matched rows to verify"
assert np.allclose(merged["Amount_scaled"], merged["Amount_chk"], atol=1e-6)
assert np.allclose(merged["Time_scaled"], merged["Time_chk"], atol=1e-6)
print(f"Scaling reproduces X_test exactly on {len(merged)} uniquely matched rows.")

out = ROOT / "models" / "scaler_params.json"
out.write_text(json.dumps(params, indent=2))
print(f"Verified against X_test and saved {out}")
print(json.dumps(params, indent=2))
