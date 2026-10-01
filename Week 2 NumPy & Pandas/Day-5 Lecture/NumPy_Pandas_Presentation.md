---
title: NumPy & Pandas
subtitle: Internship Task — Tech Prime Pvt. Limited
author: Ishfaq Khan
date: August 2026
---

# NumPy & Pandas
## Arrays · Indexing · DataFrame Operations · Merge · GroupBy

**Presented by:** Ishfaq Khan
**Role:** AI/ML Engineer Intern
**Organization:** Tech Prime Pvt. Limited, Islamabad
**Week Focus:** NumPy & Pandas Fundamentals

---

## Agenda

1. Why NumPy & Pandas?
2. NumPy Arrays
3. Indexing & Slicing
4. Pandas DataFrame Basics
5. DataFrame Operations
6. Merging & Joining Data
7. GroupBy — Split, Apply, Combine
8. Practical workflow example
9. Key takeaways

---

## 1. Why NumPy & Pandas?

- **NumPy** — the foundation of numerical computing in Python
  - Fast, memory-efficient array operations (built on C)
  - Powers nearly every other data/ML library (Pandas, Scikit-learn, TensorFlow)
- **Pandas** — built on top of NumPy for structured, labeled data
  - Works with tabular data (rows & columns) like a spreadsheet or SQL table
  - Core tool for data cleaning, transformation, and analysis

`NumPy → raw numerical arrays` &nbsp;|&nbsp; `Pandas → labeled, tabular data built on NumPy`

---

## 2. NumPy Arrays

### 2.1 Creating Arrays

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.zeros((3, 3))
c = np.ones((2, 4))
d = np.arange(0, 10, 2)          # start, stop, step
e = np.linspace(0, 1, 5)         # 5 evenly spaced values
f = np.random.rand(3, 3)         # random values
```

### 2.2 Key Array Attributes

```python
a.shape      # dimensions
a.ndim       # number of dimensions
a.dtype      # data type
a.size       # total number of elements
```

### 2.3 Why Arrays Instead of Python Lists?
- Vectorized operations — no explicit loops needed
- Much faster for large-scale numerical computation
- Supports broadcasting (operating on arrays of different shapes)

```python
arr = np.array([1, 2, 3])
arr * 2          # [2, 4, 6] — no loop required
arr + np.array([10, 20, 30])
```

---

## 3. Indexing & Slicing

### 3.1 NumPy Indexing

```python
arr = np.array([10, 20, 30, 40, 50])

arr[0]          # 10
arr[-1]         # 50
arr[1:4]        # [20, 30, 40]
arr[arr > 20]   # Boolean/conditional indexing → [30, 40, 50]
```

### 3.2 2D Array Indexing

```python
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])

matrix[0, 1]      # 2 → row 0, column 1
matrix[:, 0]      # first column → [1,4,7]
matrix[1, :]      # second row → [4,5,6]
```

### 3.3 Pandas Indexing (`loc` vs `iloc`)

```python
df.loc[0, "Name"]      # label-based access
df.iloc[0, 1]           # position-based access
df.loc[df["Age"] > 25]  # conditional row selection
```

---

## 4. Pandas DataFrame Basics

```python
import pandas as pd

df = pd.read_csv("data.csv")

df.head()        # first 5 rows
df.tail()        # last 5 rows
df.info()        # column types & non-null counts
df.describe()    # statistical summary
df.shape         # (rows, columns)
df.columns       # column names
df.dtypes        # data types per column
```

- A **Series** = single labeled column (1D)
- A **DataFrame** = collection of Series sharing an index (2D table)

---

## 5. DataFrame Operations

### 5.1 Selecting & Filtering

```python
df["Salary"]                       # select a column
df[["Name", "Salary"]]             # select multiple columns
df[df["Salary"] > 50000]           # filter rows by condition
```

### 5.2 Adding, Modifying & Dropping Columns

```python
df["Bonus"] = df["Salary"] * 0.1
df.rename(columns={"Salary": "Monthly_Salary"}, inplace=True)
df.drop(columns=["Bonus"], inplace=True)
```

### 5.3 Sorting & Applying Functions

```python
df.sort_values(by="Salary", ascending=False)
df["Salary"].apply(lambda x: x * 1.05)   # apply a custom function
```

### 5.4 Handling Missing Data

```python
df.isnull().sum()
df.fillna(df["Salary"].mean(), inplace=True)
df.dropna(inplace=True)
```

---

## 6. Merging & Joining Data

### 6.1 `merge()` — SQL-style joins

```python
employees = pd.DataFrame({"emp_id": [1,2,3], "name": ["Ali","Sara","Bilal"]})
salaries  = pd.DataFrame({"emp_id": [1,2,4], "salary": [50000,60000,55000]})

pd.merge(employees, salaries, on="emp_id", how="inner")  # matching rows only
pd.merge(employees, salaries, on="emp_id", how="left")   # keep all left rows
pd.merge(employees, salaries, on="emp_id", how="outer")  # keep all rows from both
```

| Join Type | Result |
|---|---|
| `inner` | Only matching keys in both DataFrames |
| `left` | All rows from left + matches from right |
| `right` | All rows from right + matches from left |
| `outer` | All rows from both, filling gaps with NaN |

### 6.2 `concat()` — Stacking DataFrames

```python
pd.concat([df1, df2], axis=0)   # stack rows (vertically)
pd.concat([df1, df2], axis=1)   # stack columns (horizontally)
```

---

## 7. GroupBy — Split, Apply, Combine

### 7.1 The Concept

`GroupBy` follows a three-step process:
1. **Split** the data into groups based on a key
2. **Apply** an aggregation function to each group
3. **Combine** the results into a new DataFrame

### 7.2 Example

```python
df.groupby("Department")["Salary"].mean()
df.groupby("Department")["Salary"].agg(["mean", "max", "min", "count"])
df.groupby(["Department", "Gender"])["Salary"].sum()
```

### 7.3 Common Aggregations

```python
df.groupby("Department").agg(
    avg_salary=("Salary", "mean"),
    total_employees=("Name", "count")
).reset_index()
```

---

## 8. Practical Workflow Example

1. **Load data** — `pd.read_csv()`
2. **Inspect** — `.info()`, `.describe()`, `.head()`
3. **Clean** — handle missing values, fix dtypes
4. **Transform** — create new columns, filter rows
5. **Combine** — merge with related datasets (e.g., employee + salary tables)
6. **Aggregate** — `groupby()` to summarize by category (e.g., average salary per department)
7. **Export/report** — save cleaned & summarized data for the next stage (EDA/visualization)

---

## 9. Key Takeaways

- **NumPy arrays** are the fast, vectorized foundation for numerical computing in Python
- **Pandas DataFrames** bring labeled, tabular structure on top of NumPy
- **`loc`/`iloc`** give precise label- and position-based access to data
- **`merge()`** combines related datasets like SQL joins; **`concat()`** stacks them
- **`groupby()`** is essential for summarizing data by category — split, apply, combine
- These tools form the backbone of every data cleaning, EDA, and feature engineering step in the ML pipeline

---

## Thank You

**Ishfaq Khan**
AI/ML Engineer Intern — Tech Prime Pvt. Limited
GitHub: github.com/ishfaqkhan1122
LinkedIn: linkedin.com/in/ishfaq-khan-814780316
