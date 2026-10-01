---
title: Decision Trees
subtitle: Internship Task — Tech Prime Pvt. Limited
author: Ishfaq Khan
date: August 2026
---

# Decision Trees
### Simple English + Roman Urdu Explanation with Examples

**Author:** Ishfaq Khan — AI/ML Engineer Intern, Tech Prime Pvt. Limited

---

## 1. What is a Decision Tree?

**Simple English:** A Decision Tree is a machine learning model that makes predictions by asking a series of simple **Yes/No questions**, like a flowchart, until it reaches a final answer.

**Roman Urdu:** Decision Tree ek machine learning model hai jo prediction karne ke liye lagataar simple **Haan/Nahi sawalat** poochta hai, bilkul flowchart ki tarah, jab tak aakhri jawab tak na pohanch jaye.

**Example / Misaal:**
- Is income > 50,000? → Yes → Is age > 30? → Yes → "Approve loan"
- Kya income 50,000 se zyada hai? → Haan → Kya age 30 se zyada hai? → Haan → "Loan approve karo"

---

## 2. How It Works

**Simple English:** The tree starts at the top with all the data (the **root node**). At each step, it splits the data into groups based on a feature and a condition (e.g., "Age > 30?"). It keeps splitting until it reaches a final decision, called a **leaf node**.

**Roman Urdu:** Tree sab se upar (root node) se shuru hota hai, jahan sara data hota hai. Har step par, ye data ko ek feature aur condition ke zariye groups mein split karta hai (jaise "Age > 30?"). Ye split karta rehta hai jab tak aakhri decision, jise **leaf node** kehte hain, tak na pohanche.

**Key Terms:**
- **Root node** — the very first split, at the top of the tree — sab se pehla split, tree ke sab se upar
- **Branch** — a path from one decision to the next — ek decision se doosre tak ka raasta
- **Leaf node** — the final answer/prediction at the end of a branch — branch ke aakhir mein aakhri jawab
- **Splitting criteria** — how the tree decides the best question to ask (e.g., **Gini impurity** or **entropy**) — tree ye kaise decide karta hai ke kaunsa sawal poochna behtar hai

---

## 3. Example Code

```python
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

tree_model = DecisionTreeClassifier(max_depth=4, random_state=42)
tree_model.fit(X_train, y_train)

predictions = tree_model.predict(X_test)

plt.figure(figsize=(12, 6))
plot_tree(tree_model, feature_names=X.columns, class_names=["No", "Yes"], filled=True)
plt.show()
```

**Roman Urdu note:** `max_depth` batata hai ke tree kitni gehri (deep) ja sakti hai. Isay control karna zaroori hai, warna tree bohot pechida ho sakti hai.

---

## 4. Real-Life Pakistani Example

**Simple English:** A bank in Islamabad wants to decide whether to approve a loan, based on the customer's income and credit history.

**Roman Urdu:** Islamabad mein ek bank ye decide karna chahta hai ke loan approve karna hai ya nahi, customer ki income aur credit history dekh kar.

```python
# Features: income, credit_score
new_applicant = [[45000, 720]]
prediction = tree_model.predict(new_applicant)
print("Loan approved?", "Yes" if prediction[0] == 1 else "No")
```

The tree might internally learn something like: "If income > 40,000 AND credit_score > 700, approve the loan" — a Decision Tree jaisi banayi hui condition — "Agar income 40,000 se zyada aur credit_score 700 se zyada ho, to loan approve karo."

---

## 5. Advantages & Disadvantages

**Simple English — Advantages:**
- Very easy to understand and explain — even to non-technical people
- No need for feature scaling
- Can handle both numeric and categorical data
- Naturally captures non-linear patterns

**Roman Urdu — Faide:**
- Samajhna aur explain karna bohot aasan hai — ghair-technical logon ke liye bhi
- Feature scaling ki zaroorat nahi
- Numeric aur categorical dono tarah ka data handle kar sakta hai
- Non-linear patterns ko aasani se pakarta hai

**Simple English — Disadvantages:**
- Easily **overfits** if allowed to grow too deep — memorizes training data instead of learning general patterns
- Small changes in data can produce a very different tree (unstable)

**Roman Urdu — Nuqsanat:**
- Agar tree ko bohot gehra badhne diya jaye to **overfitting** ho jati hai — training data ko yaad kar leta hai, general pattern nahi seekhta
- Data mein choti tabdeeli se bhi bilkul mukhtalif tree ban sakti hai (unstable)

---

## 6. When to Use Decision Trees

**Simple English:** Use a Decision Tree when you want a model that's easy to explain to others (like managers or clients), and when your data has clear, rule-like patterns.

**Roman Urdu:** Decision Tree tab use karein jab aapko doosron ko (jaise managers ya clients ko) asaani se samjhaana ho, aur jab data mein saaf, rule jaise patterns hon.

---

## 7. Key Takeaways / Ahem Baatein

- A Decision Tree makes predictions through a series of Yes/No splits — Decision Tree lagataar Haan/Nahi splits se prediction karta hai
- It is easy to interpret but prone to overfitting if too deep — samajhna aasan hai lekin bohot gehra hone par overfitting hoti hai
- Controlling `max_depth` helps keep the tree simple and generalizable — `max_depth` control karne se tree simple aur general rehta hai

---

**Ishfaq Khan**
AI/ML Engineer Intern — Tech Prime Pvt. Limited
