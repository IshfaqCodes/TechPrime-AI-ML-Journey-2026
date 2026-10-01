---
title: Visualization & Exploratory Data Analysis (EDA)
subtitle: Internship Task — Tech Prime Pvt. Limited
author: Ishfaq Khan
date: August 2026
---

# Visualization & EDA
## Matplotlib · Exploratory Data Analysis · Data Cleaning · Correlation Analysis

**Presented by:** Ishfaq Khan
**Role:** AI/ML Engineer Intern
**Organization:** Tech Prime Pvt. Limited, Islamabad
**Week Focus:** EDA & Visualization

---

## Agenda

1. What is Exploratory Data Analysis (EDA)?
2. EDA's place in the ML pipeline
3. Data Cleaning fundamentals
4. Data Visualization with Matplotlib
5. Correlation Analysis
6. Worked example — from raw data to insight
7. Common EDA mistakes to avoid
8. Key insights & takeaways
9. Tools & libraries used
10. Conclusion

---

## 1. What is EDA?

- **Exploratory Data Analysis (EDA)** is the process of investigating a dataset to understand its structure, quality, and relationships *before* modeling.
- Combines **statistical summaries** with **visual methods**.
- Core questions EDA answers:
  - What does the data actually look like?
  - Are there missing values, duplicates, or outliers?
  - What is the distribution of each variable?
  - How do variables relate to one another?
  - What assumptions is it safe to make going into modeling?

> "You can't trust a model built on data you don't understand. EDA is how you earn that trust."

---

## 2. EDA's Place in the ML Pipeline

`Raw Data → Data Cleaning → EDA → Feature Engineering → Modeling → Evaluation`

- Skipping EDA is one of the most common causes of poor model performance
- A well-run EDA phase:
  - Catches data quality issues **before** they corrupt a model
  - Informs which features are worth engineering or dropping
  - Builds intuition that guides algorithm choice later on
- Rule of thumb: **60–70% of a real-world data science project is spent on cleaning and understanding data**, not modeling

---

## 3. Data Cleaning Fundamentals

### 3.1 Common Data Issues

| Issue | Example | Typical Fix |
|---|---|---|
| Missing values | `NaN` in `Age` column | Impute (mean/median/mode) or drop |
| Duplicates | Same customer row twice | `drop_duplicates()` |
| Wrong data type | `"25"` instead of `25` | `astype()` conversion |
| Inconsistent labels | `"Male"`, `"male"`, `"M"` | Standardize with `.str.lower()` / mapping |
| Outliers | Salary = 9,999,999 by data-entry error | IQR / Z-score detection, cap or remove |
| Structural noise | Extra whitespace, mixed date formats | `.str.strip()`, `pd.to_datetime()` |

### 3.2 Handling Missing Values

```python
df.isnull().sum()                          # count missing values per column
df["Age"].fillna(df["Age"].median(), inplace=True)
df.dropna(subset=["Salary"], inplace=True)  # drop rows missing critical fields
```

### 3.3 Handling Duplicates & Outliers

```python
df.drop_duplicates(inplace=True)

Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1
df = df[(df["Salary"] >= Q1 - 1.5*IQR) & (df["Salary"] <= Q3 + 1.5*IQR)]
```

### 3.4 Quick Data Cleaning Checklist

- [ ] Checked shape, dtypes, and column names
- [ ] Counted and handled missing values
- [ ] Removed duplicate rows
- [ ] Fixed inconsistent categorical labels
- [ ] Detected and treated outliers
- [ ] Verified data types match expectations

---

## 4. Data Visualization with Matplotlib

### 4.1 Why Matplotlib?

- The foundational plotting library in Python — Seaborn and Pandas `.plot()` are both built on it
- Highly customizable: figure size, colors, labels, annotations, subplots
- Produces static, publication-quality charts

### 4.2 Common Plot Types Used in EDA

| Plot Type | Purpose | Best For |
|---|---|---|
| Histogram | Distribution of one numeric variable | Spotting skew, spread |
| Boxplot | Median, quartiles, outliers | Outlier detection |
| Scatter plot | Relationship between two numeric variables | Spotting correlation/trend |
| Bar chart | Comparison across categories | Categorical summaries |
| Line chart | Trend over time/sequence | Time-series data |
| Heatmap | Correlation matrix | Multivariate relationships |
| Pairplot | All pairwise numeric relationships at once | Quick multivariate overview |

### 4.3 Example: Clean, Well-Labeled Plots

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")
plt.style.use("seaborn-v0_8-whitegrid")   # clean, readable style

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Age"], bins=20, color="steelblue", edgecolor="black")
plt.title("Age Distribution", fontsize=13, fontweight="bold")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Boxplot for outlier detection
plt.figure(figsize=(6, 4))
plt.boxplot(df["Salary"], vert=False)
plt.title("Salary Spread & Outliers")
plt.xlabel("Salary")
plt.tight_layout()
plt.show()

# Multiple subplots in one figure
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].hist(df["Age"], bins=15, color="darkorange")
axes[0].set_title("Age Distribution")
axes[1].scatter(df["Age"], df["Salary"], alpha=0.6, color="teal")
axes[1].set_title("Age vs Salary")
plt.tight_layout()
plt.show()
```

### 4.4 Good Practice Tips

- Always label axes and add a title — an unlabeled chart tells no story
- Use `figsize` and `tight_layout()` for readable, presentation-ready plots
- Prefer subplots over separate scattered figures when comparing related variables
- Choose color intentionally — avoid overly bright or clashing palettes

---

## 5. Correlation Analysis

### 5.1 What is Correlation?

- Measures the strength and direction of a **linear relationship** between two numeric variables
- Pearson correlation coefficient ranges from **-1 to +1**
  - **+1** → strong positive relationship
  - **-1** → strong negative relationship
  - **0** → no linear relationship

### 5.2 Why It Matters

- Identifies **redundant or highly correlated features** (multicollinearity risk)
- Helps prioritize which features are most relevant to the target variable
- Directly informs feature selection and engineering decisions

### 5.3 Example: Correlation Heatmap

```python
import seaborn as sns

corr_matrix = df.corr(numeric_only=True)

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Feature Correlation Heatmap", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.show()
```

**Important caveat:** correlation shows statistical association, not causation. Two variables can move together without one causing the other (e.g., ice cream sales and drowning incidents both rise with summer heat).

---

## 6. Worked Example — From Raw Data to Insight

A condensed walkthrough combining every step above:

1. **Load** — `df = pd.read_csv("employee_data.csv")`
2. **Inspect** — `df.info()`, `df.describe()`, `df.head()`
3. **Clean** — fill missing `Salary` with median, drop duplicate employee IDs, standardize `Department` labels
4. **Visualize distributions** — histogram of `Age`, boxplot of `Salary` to catch outliers
5. **Explore relationships** — scatter plot of `Experience` vs `Salary`
6. **Correlate** — heatmap reveals `Experience` and `Salary` are strongly positively correlated (r ≈ 0.82), while `Age` and `Performance_Score` show almost no relationship
7. **Conclusion** — `Experience` is a strong candidate feature for predicting `Salary`; `Age` alone likely won't add much predictive value

This mirrors the exact workflow expected before moving into regression modeling in the following internship week.

---

## 7. Common EDA Mistakes to Avoid

- Jumping straight to modeling without checking data quality first
- Ignoring outliers instead of investigating *why* they exist
- Treating correlation as proof of causation
- Producing unlabeled or unscaled charts that mislead the viewer
- Only looking at summary statistics without visualizing the distribution (e.g., `mean` alone can hide a bimodal distribution)

---

## 8. Key Insights & Takeaways

- EDA is not optional — it is the foundation of trustworthy analysis and modeling
- A clean dataset directly improves model accuracy and reliability
- Visualization turns raw numbers into patterns a human can actually reason about
- Correlation analysis helps avoid redundant or misleading features
- Disciplined EDA habits save significant debugging time later in the pipeline

---

## 9. Tools & Libraries Used

- **Pandas** — data loading, cleaning, and manipulation
- **NumPy** — numerical operations underlying Pandas
- **Matplotlib** — core visualization engine
- **Seaborn** — statistical visualization (heatmaps, pairplots, style presets)
- **Jupyter Notebook** — interactive analysis environment

---

## 10. Conclusion

- Completed hands-on practice with **data cleaning**, **visualization**, and **correlation analysis** as part of the Week 3 EDA & Visualization module of the Tech Prime AI/ML Engineer internship
- Applied Matplotlib and Seaborn to explore and visualize a real dataset end-to-end
- Built a repeatable, checklist-driven EDA workflow to apply on future datasets
- **Next step:** carry these cleaned, well-understood features into feature engineering and regression modeling

---

## Thank You

**Ishfaq Khan**
AI/ML Engineer Intern — Tech Prime Pvt. Limited
GitHub: github.com/ishfaqkhan1122
LinkedIn: linkedin.com/in/ishfaq-khan-814780316
