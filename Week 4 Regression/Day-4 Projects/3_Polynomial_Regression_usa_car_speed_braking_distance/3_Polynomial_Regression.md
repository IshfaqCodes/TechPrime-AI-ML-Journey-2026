# Polynomial Regression — Car Speed vs Braking Distance (USA)

## Files in this folder
- `3_Polynomial_Regression.ipynb` — notebook
- `usa_car_speed_braking_distance.csv` — dataset (250 rows)

## Dataset
Synthetic USA road-safety physics data:
| Column | Description |
|---|---|
| `speed_mph` | Car speed in miles per hour |
| `braking_distance_ft` | Distance (feet) needed to stop after braking |

## What this notebook covers
1. Loading and exploring the dataset
2. Visualizing the raw data — the curved (non-linear) pattern is visible immediately
3. Fitting a Simple Linear (straight-line) model as a baseline
4. Fitting a Polynomial Regression model (degree = 2)
5. Evaluating and comparing both models (R², MAE, RMSE)
6. Side-by-side plot of the linear line vs the polynomial curve
7. Predicting braking distance at various speeds with both models, showing how the linear model underestimates distance at high speed

## Why this dataset
Braking distance grows roughly with the square of speed (a real physics relationship), so it needed a dataset from a different context than the Pakistan datasets — one with a genuine curve — to clearly demonstrate why and when Polynomial Regression outperforms a straight-line fit.

## Result summary
- Polynomial (degree=2) fit has a noticeably higher R² and lower error than the simple linear fit
- The gap between the two models grows at higher speeds — the linear model is unsafe to rely on there

## Requirements
```
pandas
numpy
matplotlib
scikit-learn
```
