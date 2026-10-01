---
title: Logistic Regression
subtitle: Internship Task — Tech Prime Pvt. Limited
author: Ishfaq Khan
date: August 2026
---

# Logistic Regression
### Simple English + Roman Urdu Explanation with Examples

**Author:** Ishfaq Khan — AI/ML Engineer Intern, Tech Prime Pvt. Limited

---

## 1. What is Logistic Regression?

**Simple English:** Logistic Regression is a machine learning method used to predict a **category**, like "Yes" or "No", not a number. Even though the name has "Regression" in it, it is actually used for **classification** problems.

**Roman Urdu:** Logistic Regression ek machine learning tareeqa hai jo hume ek **category** predict karne mein madad karta hai, jaise "Haan" ya "Nahi". Naam mein "Regression" hone ke bawajood, ye asal mein **classification** ke liye use hota hai.

**Example / Misaal:**
- Will a customer buy a product? (Yes / No)
- Kya customer product khareedega? (Haan / Nahi)
- Is an email spam or not spam?
- Kya email spam hai ya nahi?

---

## 2. How It Works

**Simple English:** Logistic Regression first calculates a number using input features, then passes that number through a special curve called the **sigmoid function**. This curve turns any number into a value between **0 and 1**, which represents a **probability**.

**Roman Urdu:** Logistic Regression pehle input features se ek number nikalta hai, phir us number ko ek khaas curve se guzarta hai jise **sigmoid function** kehte hain. Ye curve kisi bhi number ko **0 aur 1** ke darmiyan value mein badal deta hai, jo ek **probability** ko zahir karti hai.

**Rule / Qaida:**
- If probability > 0.5 → predict class 1 (e.g., "Yes")
- Agar probability > 0.5 ho → class 1 predict hoga (jaise "Haan")
- If probability ≤ 0.5 → predict class 0 (e.g., "No")
- Agar probability ≤ 0.5 ho → class 0 predict hoga (jaise "Nahi")

---

## 3. Example Code

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# X = features (like age, income), y = target (like buy/not buy)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)   # probability for each class

print("Accuracy:", accuracy_score(y_test, predictions))
```

**Roman Urdu note:** `fit()` model ko training data se seekhne (learn karne) ke liye use hota hai, aur `predict()` naye data par prediction dene ke liye use hota hai.

---

## 4. Real-Life Pakistani Example

**Simple English:** Imagine a mobile phone company wants to know if a customer will renew their Jazz or Zong package or not, based on their usage minutes and monthly spending.

**Roman Urdu:** Faraz karein ke ek mobile company ye jaanna chahti hai ke customer apna Jazz ya Zong package renew karega ya nahi, uske usage minutes aur monthly kharch ke hisaab se.

```python
# Features: minutes_used, monthly_spending
# Target: renewed (1 = Yes, 0 = No)

model.fit(X_train, y_train)
new_customer = [[300, 1500]]   # 300 minutes, Rs. 1500 spending
prediction = model.predict(new_customer)
print("Will renew?" , "Yes" if prediction[0] == 1 else "No")
```

---

## 5. Advantages & Disadvantages

**Simple English — Advantages:**
- Easy to understand and explain
- Fast to train, even on large data
- Gives a probability, not just a hard Yes/No answer
- Good starting/baseline model for classification problems

**Roman Urdu — Faide:**
- Samajhna aur explain karna aasan hai
- Bade data par bhi jaldi train hota hai
- Sirf Haan/Nahi nahi, balke probability bhi deta hai
- Classification problems ke liye acha shuruaati model hai

**Simple English — Disadvantages:**
- Works best only when classes can be separated by a roughly straight line
- Struggles with very complex, non-linear patterns in data

**Roman Urdu — Nuqsanat:**
- Best tab kaam karta hai jab classes ek seedhi line se alag ho sakti hain
- Bohot pechida (complex), ghair-seedhi (non-linear) patterns mein kamzor perform karta hai

---

## 6. When to Use Logistic Regression

**Simple English:** Use it when you need a fast, simple, and interpretable model for a Yes/No (or multi-category) prediction, and your data doesn't have a very complicated pattern.

**Roman Urdu:** Jab aapko ek fast, simple, aur samajh aane wala model chahiye ho Haan/Nahi (ya kai categories) predict karne ke liye, aur data mein bohot pechida pattern na ho, tab Logistic Regression use karein.

---

## 7. Key Takeaways / Ahem Baatein

- Logistic Regression predicts categories, not numbers — Logistic Regression numbers nahi, categories predict karta hai
- It uses the sigmoid function to turn a number into a probability — ye sigmoid function se number ko probability mein badalta hai
- It's a strong, simple baseline model for classification tasks — ye classification ke liye ek mazboot aur simple baseline model hai

---

**Ishfaq Khan**
AI/ML Engineer Intern — Tech Prime Pvt. Limited
