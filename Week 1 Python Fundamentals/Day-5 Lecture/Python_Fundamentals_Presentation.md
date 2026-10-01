---
title: Python Fundamentals
subtitle: Internship Task — Tech Prime Pvt. Limited
author: Ishfaq Khan
date: August 2026
---

# Python Fundamentals
## Variables · Data Types · Loops · Functions · OOP · File Handling

**Presented by:** Ishfaq Khan
**Role:** AI/ML Engineer Intern
**Organization:** Tech Prime Pvt. Limited, Islamabad
**Week Focus:** Python Fundamentals (Week 1)

---

## Agenda

1. Why Python for AI/ML?
2. Variables & Data Types
3. Operators
4. Control Flow & Loops
5. Functions
6. Object-Oriented Programming (OOP)
7. File Handling
8. Worked example — putting it all together
9. Common beginner mistakes to avoid
10. Key takeaways

---

## 1. Why Python for AI/ML?

- Simple, readable syntax — fast to write and debug
- Massive ecosystem: NumPy, Pandas, Matplotlib, Scikit-learn, TensorFlow, PyTorch
- Strong community support and documentation
- Interpreted language — no compilation step, quick iteration
- Industry standard for data science, machine learning, and automation

`Solid fundamentals here → everything else in the internship (NumPy, Pandas, ML models) builds directly on top of this`

---

## 2. Variables & Data Types

### 2.1 Variables

- No explicit type declaration needed — Python infers the type automatically
- Naming convention: `snake_case`, descriptive names

```python
name = "Ishfaq"
age = 21
gpa = 3.8
is_student = True
```

### 2.2 Core Data Types

| Type | Example | Description |
|---|---|---|
| `int` | `25` | Whole numbers |
| `float` | `3.14` | Decimal numbers |
| `str` | `"Bannu"` | Text |
| `bool` | `True` / `False` | Logical values |
| `list` | `[1, 2, 3]` | Ordered, mutable collection |
| `tuple` | `(1, 2, 3)` | Ordered, immutable collection |
| `dict` | `{"key": "value"}` | Key-value pairs |
| `set` | `{1, 2, 3}` | Unordered, unique values |

### 2.3 Type Checking & Conversion

```python
type(age)              # <class 'int'>
str(age)                # "25"
int("25")               # 25
float("3.14")            # 3.14
```

---

## 3. Operators

| Category | Examples |
|---|---|
| Arithmetic | `+ - * / // % **` |
| Comparison | `== != > < >= <=` |
| Logical | `and`, `or`, `not` |
| Assignment | `= += -= *= /=` |
| Membership | `in`, `not in` |

```python
x = 10
x += 5          # x = 15
result = (x > 10) and (x < 20)   # True
```

---

## 4. Control Flow & Loops

### 4.1 Conditional Statements

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"
```

### 4.2 `for` Loops

```python
for i in range(5):
    print(i)                     # 0 1 2 3 4

fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
```

### 4.3 `while` Loops

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### 4.4 Loop Control

```python
for i in range(10):
    if i == 3:
        continue      # skip this iteration
    if i == 7:
        break          # exit the loop entirely
    print(i)
```

### 4.5 Comprehensions (Pythonic Shortcuts)

```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

---

## 5. Functions

### 5.1 Defining & Calling Functions

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Ishfaq"))
```

### 5.2 Default & Keyword Arguments

```python
def calculate_area(length, width=1):
    return length * width

calculate_area(5)              # width defaults to 1
calculate_area(length=5, width=3)
```

### 5.3 `*args` and `**kwargs`

```python
def total(*numbers):
    return sum(numbers)

def show_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
```

### 5.4 Lambda Functions

```python
square = lambda x: x ** 2
add = lambda a, b: a + b
```

### 5.5 Why Functions Matter

- Avoid repeating code (DRY principle — Don't Repeat Yourself)
- Break complex logic into smaller, testable pieces
- Foundation for building reusable ML pipelines and utility scripts

---

## 6. Object-Oriented Programming (OOP)

### 6.1 Core Concepts

| Concept | Meaning |
|---|---|
| Class | Blueprint for creating objects |
| Object | An instance of a class |
| Attribute | Data stored in an object |
| Method | Function defined inside a class |
| Inheritance | A class reusing/extending another class |
| Encapsulation | Bundling data and behavior together |

### 6.2 Defining a Class

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def show_details(self):
        return f"{self.name} - GPA: {self.gpa}"

s1 = Student("Ishfaq", 3.8)
print(s1.show_details())
```

### 6.3 Inheritance

```python
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I am {self.name}"

class Intern(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def introduce(self):
        return f"{super().introduce()}, interning at {self.company}"

i1 = Intern("Ishfaq", "Tech Prime")
print(i1.introduce())
```

### 6.4 Why OOP Matters in ML Projects

- Scikit-learn, TensorFlow, and PyTorch are all built around class-based APIs (`model.fit()`, `model.predict()`)
- Understanding OOP makes it far easier to read library source code and build custom pipelines/classes

---

## 7. File Handling

### 7.1 Reading & Writing Text Files

```python
# Writing to a file
with open("notes.txt", "w") as file:
    file.write("Internship Week 1 - Python Fundamentals")

# Reading a file
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```

### 7.2 File Modes

| Mode | Meaning |
|---|---|
| `"r"` | Read (default) |
| `"w"` | Write (overwrites existing content) |
| `"a"` | Append (adds to existing content) |
| `"r+"` | Read and write |

### 7.3 Working with CSV Files

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

### 7.4 Why `with open(...)` Instead of `open()`

- Automatically closes the file, even if an error occurs
- Prevents memory leaks and file-lock issues — considered Pythonic best practice

---

## 8. Worked Example — Putting It All Together

A small script combining variables, loops, functions, OOP, and file handling:

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

employees = [
    Employee("Ali", 50000),
    Employee("Sara", 60000),
    Employee("Bilal", 55000),
]

with open("payroll_report.txt", "w") as file:
    for emp in employees:
        line = f"{emp.name}: Annual Salary = {emp.annual_salary()}\n"
        file.write(line)
        print(line.strip())
```

This mirrors a realistic pattern: define a class to model an entity, loop through records, compute derived values with a method, and persist results to a file — the same shape used later for logging model results and reports.

---

## 9. Common Beginner Mistakes to Avoid

- Using mutable default arguments (e.g., `def f(items=[])`) — leads to unexpected shared state
- Forgetting `self` as the first parameter in instance methods
- Not closing files (always prefer `with open(...)`)
- Comparing values with `is` instead of `==` (`is` checks identity, not equality)
- Overusing global variables instead of passing values through functions

---

## 10. Key Takeaways

- Strong fundamentals in variables, data types, and control flow are the base every later topic builds on
- Functions keep code reusable, readable, and testable
- OOP is essential for understanding how ML libraries like Scikit-learn are structured
- File handling with `with open(...)` is the safe, Pythonic standard for reading/writing data
- These fundamentals directly support the NumPy, Pandas, and EDA work covered in later internship weeks

---

## Thank You

**Ishfaq Khan**
AI/ML Engineer Intern — Tech Prime Pvt. Limited
GitHub: github.com/ishfaqkhan1122
LinkedIn: linkedin.com/in/ishfaq-khan-814780316
