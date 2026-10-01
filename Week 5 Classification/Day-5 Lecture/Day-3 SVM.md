---
title: Support Vector Machine (SVM)
subtitle: Internship Task — Tech Prime Pvt. Limited
author: Ishfaq Khan
date: August 2026
---

# Support Vector Machine (SVM)
### Simple English + Roman Urdu Explanation with Examples

**Author:** Ishfaq Khan — AI/ML Engineer Intern, Tech Prime Pvt. Limited

---

## 1. What is SVM?

**Simple English:** SVM is a machine learning model that separates different categories of data by drawing the **best possible boundary line (or curve)** between them, keeping the biggest possible gap from both sides.

**Roman Urdu:** SVM ek machine learning model hai jo data ki mukhtalif categories ko alag karne ke liye unke darmiyan **behtareen boundary line (ya curve)** khenchta hai, dono taraf se sab se bara gap rakh kar.

**Simple idea / Simple soch:**
- Imagine drawing a line between two groups of students standing in a field, keeping it as far as possible from both groups
- Faraz karein ek maidan mein khare do groups ke darmiyan ek line khenchna, aur usay dono groups se jitna ho sake door rakhna

---

## 2. How It Works

**Simple English:**
- SVM finds the boundary, called a **hyperplane**, that separates classes with the **maximum margin** (largest possible gap)
- The data points closest to this boundary are called **support vectors** — they are the most important points, because they decide where the boundary sits
- For data that cannot be separated with a straight line, SVM uses something called the **kernel trick** to map the data into a higher dimension, where it becomes separable

**Roman Urdu:**
- SVM wo boundary dhoondta hai, jise **hyperplane** kehte hain, jo classes ko **maximum margin** (sab se bara gap) ke saath alag karti hai
- Is boundary ke sab se qareeb data points ko **support vectors** kehte hain — ye sab se ahem points hote hain, kyunke ye tay karte hain boundary kahan hogi
- Jo data seedhi line se alag nahi ho sakta, uske liye SVM **kernel trick** use karta hai, jo data ko ek higher dimension mein le jata hai jahan wo alag ho sakta hai

**Key Terms:**
- **Hyperplane** — the separating boundary — alag karne wali boundary
- **Margin** — the gap between the boundary and the nearest points of each class — boundary aur har class ke qareeb tareen points ke darmiyan gap
- **Support vectors** — the closest points that define the boundary — sab se qareeb points jo boundary ko tay karte hain
- **Kernel** — a method to handle curved/non-linear boundaries (e.g., `linear`, `rbf`, `poly`) — curved/non-linear boundaries handle karne ka tareeqa

---

## 3. Example Code

```python
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling is important because SVM is distance-based
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

svm_model = SVC(kernel="rbf", C=1.0, gamma="scale")
svm_model.fit(X_train_scaled, y_train)

predictions = svm_model.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, predictions))
```

**Roman Urdu note:** `C` batata hai model kitna sakht (strict) ho har ghalti par — bara `C` matlab kam ghaltiyon ki ijazat, chota `C` matlab zyada nirmi (flexibility).

---

## 4. Real-Life Pakistani Example

**Simple English:** A bank wants to detect if a transaction is fraudulent or genuine, using features like transaction amount and location distance from the customer's usual city.

**Roman Urdu:** Ek bank ye pata karna chahta hai ke transaction fraud hai ya asli, features jese transaction amount aur customer ke arafi shehar se location ki doori ka istemal karte hue.

```python
# Features: transaction_amount, distance_from_usual_location
new_transaction = [[45000, 320]]
new_transaction_scaled = scaler.transform(new_transaction)
prediction = svm_model.predict(new_transaction_scaled)
print("Fraudulent?", "Yes" if prediction[0] == 1 else "No")
```

---

## 5. Advantages & Disadvantages

**Simple English — Advantages:**
- Works very well when there is a clear gap/margin between classes
- Effective even with a high number of features
- The kernel trick lets it handle complex, non-linear boundaries

**Roman Urdu — Faide:**
- Bohot acha kaam karta hai jab classes ke darmiyan saaf gap ho
- Zyada features hone par bhi acha kaam karta hai
- Kernel trick se pechida, non-linear boundaries bhi handle kar leta hai

**Simple English — Disadvantages:**
- Can be slow to train on very large datasets
- Requires feature scaling, or results will be misleading
- Choosing the right kernel and settings (`C`, `gamma`) can take experimentation
- Harder to interpret than simpler models like Logistic Regression or Decision Trees

**Roman Urdu — Nuqsanat:**
- Bohot bare datasets par train hone mein waqt lag sakta hai
- Feature scaling zaroori hai, warna results ghalat ho sakte hain
- Sahi kernel aur settings (`C`, `gamma`) chunne ke liye experiment karna parta hai
- Logistic Regression ya Decision Tree jaise simple models ke muqable mein samajhna mushkil hai

---

## 6. When to Use SVM

**Simple English:** Use SVM when your dataset is small-to-medium sized, features are scaled, and you expect a clear separation (margin) between classes, especially when that separation may be curved rather than a straight line.

**Roman Urdu:** SVM tab use karein jab aapka dataset chota se drmiyana size ka ho, features scaled hon, aur aapko lage ke classes ke darmiyan saaf faasla (margin) hai, khaas kar jab wo faasla seedha nahi balke curved ho.

---

## 7. Key Takeaways / Ahem Baatein

- SVM separates classes by finding the boundary with the maximum margin — SVM classes ko maximum margin wali boundary dhoond kar alag karta hai
- Support vectors are the key points that define this boundary — support vectors wo ahem points hain jo is boundary ko tay karte hain
- The kernel trick allows SVM to handle non-linear, curved relationships — kernel trick SVM ko non-linear, curved relationships handle karne deta hai

---

**Ishfaq Khan**
AI/ML Engineer Intern — Tech Prime Pvt. Limited
