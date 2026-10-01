---
title: Regression
subtitle: Internship Task — Tech Prime Pvt. Limited
author: Ishfaq Khan
date: August 2026
---

# Regression
## Linear Regression · Polynomial Regression · Evaluation Metrics

**Presented by:** Ishfaq Khan
**Role:** AI/ML Engineer Intern
**Organization:** Tech Prime Pvt. Limited, Islamabad
**Week Focus:** Regression

---

## Agenda

1. What is Regression?
2. Linear Regression
3. Polynomial Regression
4. Evaluation Metrics
5. Train/Test Split & Overfitting
6. Worked example — predicting a target from data
7. Common mistakes to avoid
8. Key takeaways

---

## 1. What is Regression?

- **Regression** is a supervised machine learning technique used to predict a **continuous numeric value** (not a category).
- Learns the relationship between one or more **independent variables (features)** and a **dependent variable (target)**.
- Examples: predicting house price, salary, temperature, sales revenue.

`Features (X) → Regression Model → Predicted continuous value (y)`

| Regression | Classification |
|---|---|
| Predicts a number (price, score) | Predicts a category (spam/not spam) |
| Output is continuous | Output is discrete |
| Example: predict salary | Example: predict pass/fail |

---

## 2. Linear Regression

### 2.1 Concept

- Assumes a **straight-line relationship** between input(s) and output.
- Simple Linear Regression (1 feature): `y = mx + b`
  - `m` = slope (how much y changes per unit of x)
  - `b` = intercept (value of y when x = 0)
- Multiple Linear Regression (many features): `y = b0 + b1*x1 + b2*x2 + ... + bn*xn`
- The model learns the best-fit line by minimizing the **error** between predicted and actual values (usually using **Ordinary Least Squares**).

### 2.2 Example Code

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("house_prices.csv")
X = df[["Area", "Bedrooms"]]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
```

### 2.3 When to Use Linear Regression

- Relationship between features and target looks roughly straight-line (check with a scatter plot first)
- Fast, simple, and easy to interpret — a good baseline model

---

## 3. Polynomial Regression

### 3.1 Concept

- Used when the relationship between features and target is **curved**, not a straight line.
- Extends linear regression by adding powers of the feature: `y = b0 + b1*x + b2*x² + b3*x³ + ...`
- Still considered a form of "linear" model, because it is linear in its **coefficients**, even though the curve itself is not straight.

### 3.2 Example Code

```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

poly_model = make_pipeline(
    PolynomialFeatures(degree=3),
    LinearRegression()
)

poly_model.fit(X_train, y_train)
predictions = poly_model.predict(X_test)
```

### 3.3 Choosing the Right Degree

| Degree | Risk |
|---|---|
| Too low (e.g., 1 for curved data) | **Underfitting** — model too simple, misses the pattern |
| Just right | Good balance — fits the true pattern well |
| Too high | **Overfitting** — model memorizes noise, fails on new data |

- Always visualize the fitted curve against actual data points to sanity-check the degree chosen.

---

## 4. Evaluation Metrics

Regression models are judged using **error-based metrics** — how far predictions are from actual values.

| Metric | Formula (concept) | What It Tells You |
|---|---|---|
| **MAE** (Mean Absolute Error) | Average of `\|actual - predicted\|` | Average error size, in original units, easy to interpret |
| **MSE** (Mean Squared Error) | Average of `(actual - predicted)²` | Penalizes large errors more heavily |
| **RMSE** (Root Mean Squared Error) | `√MSE` | Same units as target, easier to interpret than MSE |
| **R² Score** (Coefficient of Determination) | Proportion of variance explained by the model | 1.0 = perfect fit, 0 = no better than predicting the mean |

### 4.1 Example Code

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)

print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²: {r2:.2f}")
```

### 4.2 Reading the Numbers

- Lower MAE/MSE/RMSE → better predictions
- R² closer to 1 → model explains most of the variation in the target
- A high R² on training data but low R² on test data is a classic sign of **overfitting**

---

## 5. Train/Test Split & Overfitting

- Data is split into a **training set** (model learns from this) and a **test set** (used to check performance on unseen data)
- Common split: 80% train / 20% test
- **Overfitting** — model performs great on training data but poorly on new data (memorized noise instead of the pattern)
- **Underfitting** — model performs poorly on both training and test data (too simple to capture the pattern)
- **Cross-validation** — splitting data into multiple folds to get a more reliable performance estimate than a single train/test split

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5, scoring="r2")
print("Average R² across folds:", scores.mean())
```

---

## 6. Worked Example — Predicting a Target from Data

1. **Load & clean data** — handle missing values, fix types (builds on the EDA week)
2. **Explore relationships** — scatter plot of feature vs target to check if it looks linear or curved
3. **Split data** — `train_test_split(X, y, test_size=0.2)`
4. **Try Linear Regression first** — simple baseline model
5. **Check metrics** — MAE, RMSE, R² on the test set
6. **If the fit is poor and the scatter plot looks curved** — try Polynomial Regression with a low degree (2 or 3)
7. **Compare metrics** between linear and polynomial models, pick the one that generalizes best (not just the one with the lowest training error)
8. **Report results** — document the chosen model, its metrics, and why it was selected

---

## 7. Common Mistakes to Avoid

- Judging a model only on training data — always check test set performance
- Using a very high polynomial degree "to get a perfect fit" — leads to overfitting
- Forgetting to scale/prepare features consistently between training and test sets
- Relying on R² alone — a high R² does not guarantee low real-world error; check RMSE/MAE too
- Not visualizing the data before choosing linear vs polynomial regression

---

## 8. Key Takeaways

- **Linear Regression** models straight-line relationships and is a strong, interpretable baseline
- **Polynomial Regression** extends linear regression to fit curved relationships, but needs careful degree selection to avoid overfitting
- **MAE, MSE, RMSE, and R²** are the core metrics used to judge regression model quality
- Always evaluate on a **held-out test set**, not just training data
- These regression foundations lead directly into classification and more advanced ML pipelines in later internship weeks

---

## Thank You

**Ishfaq Khan**
AI/ML Engineer Intern — Tech Prime Pvt. Limited
GitHub: github.com/ishfaqkhan1122
LinkedIn: linkedin.com/in/ishfaq-khan-814780316
