---
title: K-Nearest Neighbors (KNN)
subtitle: Internship Task — Tech Prime Pvt. Limited
author: Ishfaq Khan
date: August 2026
---

# K-Nearest Neighbors (KNN)
### Simple English + Roman Urdu Explanation with Examples

**Author:** Ishfaq Khan — AI/ML Engineer Intern, Tech Prime Pvt. Limited

---

## 1. What is KNN?

**Simple English:** KNN is a machine learning method that predicts the category of a new point by looking at the categories of the points **closest to it**. It works on the simple idea: "You are similar to your neighbors."

**Roman Urdu:** KNN ek machine learning tareeqa hai jo naye point ki category predict karta hai uske **sab se qareeb (nearest)** points ki categories dekh kar. Ye is simple idea par kaam karta hai: "Aap apne neighbors jese hote hain."

**Example / Misaal:**
- If most of your close friends like cricket, you're probably a cricket fan too
- Agar aapke zyada tar qareebi dost cricket pasand karte hain, to aap bhi shayad cricket fan hain

---

## 2. How It Works

**Simple English:** KNN does not build a model in advance. When a new point needs a prediction, it:
1. Measures the **distance** from the new point to every point in the training data
2. Picks the **k closest points** (neighbors)
3. Looks at the majority category among those neighbors
4. Assigns that majority category to the new point

**Roman Urdu:** KNN pehle se koi model nahi banata. Jab naye point ke liye prediction chahiye hoti hai, to ye:
1. Naye point ki **distance** training data ke har point se napta hai
2. Sab se qareeb **k points** (neighbors) chunta hai
3. In neighbors mein sab se zyada aane wali category dekhta hai
4. Wohi category naye point ko de deta hai

**What is `k`?**
- `k` is the number of neighbors to look at — `k` un neighbors ki tadaad hai jo dekhe jaate hain
- Small `k` → sensitive to noise — Chota `k` → noise se zyada mutasir hota hai
- Large `k` → smoother but can miss finer patterns — Bara `k` → zyada smooth lekin baarik patterns miss kar sakta hai

---

## 3. Example Code

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling is important because KNN uses distance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

predictions = knn.predict(X_test_scaled)
```

**Roman Urdu note:** Scaling zaroori hai kyunke agar ek feature (jaise salary) bara ho aur dusra feature (jaise age) chota ho, to distance ka hisaab galat ho sakta hai.

---

## 4. Real-Life Pakistani Example

**Simple English:** Suppose we want to predict if a new house buyer in Rawalpindi will prefer a "Small House" or "Large House" category, based on their neighbors' income and family size in the housing dataset.

**Roman Urdu:** Faraz karein hum ye predict karna chahte hain ke Rawalpindi mein ek naya ghar khareedne wala "Chhota Ghar" pasand karega ya "Bara Ghar", uske qareebi logon ki income aur family size dekh kar.

```python
# Features: income, family_size
new_buyer = [[80000, 5]]
new_buyer_scaled = scaler.transform(new_buyer)
prediction = knn.predict(new_buyer_scaled)
print("Predicted house preference:", prediction[0])
```

---

## 5. Advantages & Disadvantages

**Simple English — Advantages:**
- Very simple to understand — no complicated math to explain
- No training phase needed — it just stores the data
- Works well when similar points really do belong to the same category

**Roman Urdu — Faide:**
- Samajhna bohot aasan hai — koi mushkil math nahi
- Training ki zaroorat nahi — ye sirf data store karta hai
- Acha kaam karta hai jab similar points waqai ek hi category ke hote hain

**Simple English — Disadvantages:**
- Slow on large datasets — it compares the new point to every stored point
- Needs feature scaling, or distance calculations become misleading
- Sensitive to irrelevant or noisy features

**Roman Urdu — Nuqsanat:**
- Bare data par slow hota hai — kyunke har point se distance calculate karta hai
- Feature scaling zaroori hai, warna distance ka hisaab ghalat ho sakta hai
- Ghair-zaroori ya noisy features se mutasir hota hai

---

## 6. When to Use KNN

**Simple English:** Use KNN for smaller datasets where you expect similar data points to share the same category, and when you want a simple, easy-to-explain model.

**Roman Urdu:** Chote datasets ke liye KNN use karein, jahan aapko lage ke similar data points ek hi category ke hain, aur jab aapko ek simple, asaan model chahiye ho.

---

## 7. Key Takeaways / Ahem Baatein

- KNN predicts based on the closest neighbors, not a learned formula — KNN qareebi neighbors dekh kar predict karta hai, koi seekhi hui formula se nahi
- Feature scaling is essential before using KNN — KNN use karne se pehle feature scaling zaroori hai
- Choosing the right `k` is important — too small or too large can hurt accuracy — sahi `k` chunna zaroori hai — bohot chota ya bohot bara accuracy kharab kar sakta hai

---

**Ishfaq Khan**
AI/ML Engineer Intern — Tech Prime Pvt. Limited
