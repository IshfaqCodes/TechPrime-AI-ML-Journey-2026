# Simple Linear Regression — Experience vs Salary (Pakistan IT Industry)

## Files in this folder
- `1_Simple_Linear_Regression.ipynb` — notebook
- `pakistan_it_experience_salary.csv` — dataset (300 rows)

## Dataset
Synthetic data of Pakistan IT professionals with two columns:
| Column | Description |
|---|---|
| `experience_years` | Years of professional experience (0–20) |
| `salary_thousand_pkr` | Monthly salary in thousand PKR |

## What this notebook covers
1. Loading and exploring the dataset
2. Visualizing the raw experience-vs-salary relationship
3. Train/test split and training a Simple Linear Regression model (1 feature → 1 target)
4. Evaluating the model (R², MAE, RMSE)
5. Plotting the fitted regression line against actual data
6. Predicting salary for new experience values (e.g. 3, 10, 20 years)

## Why this dataset
Designed with a clean, mostly linear trend so the core mechanics of Simple Linear Regression (single feature, straight-line fit) are easy to see clearly, without the noise of multiple factors.

## Result summary
- R² Score: ~0.85
- Equation: `salary ≈ intercept + slope × experience_years`

## Requirements
```
pandas
numpy
matplotlib
scikit-learn
```
