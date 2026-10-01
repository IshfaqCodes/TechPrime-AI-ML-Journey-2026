"""
=====================================================================
   OOP (Object Oriented Programming) — A to Z Concepts in Python
   Prepared for: Ishfaq Khan
=====================================================================

How to use this file:
- Har section ek naya OOP concept explain karta hai.
- Run karne ke liye, jis section ko dekhna hai uske comments parhein
  aur code ko samjhein — sab kuch top se bottom chal jayega.
"""


# =====================================================================
# 1. CLASS & OBJECT
# =====================================================================
# Class = blueprint / design (jaise makan ka naksha)
# Object = us blueprint se bana hua actual cheez (jaise asli makan)

class Student:
    pass

s1 = Student()   # object 1
s2 = Student()   # object 2

print("1. Class & Object")
print(type(s1))
print("s1 aur s2 do alag objects hain, chahe class same hai:", s1 is s2)
print("-" * 60)


# =====================================================================
# 2. CONSTRUCTOR (__init__)
# =====================================================================
# Constructor woh special method hai jo object banate hi automatically
# call ho jata hai. Python mein iska naam __init__ hota hai.

class StudentWithConstructor:
    def __init__(self):
        print("Constructor Called!")

print("2. Constructor")
s1 = StudentWithConstructor()
print("-" * 60)


# ---------------------------------------------------------------------
# 2.1 Default Constructor
# ---------------------------------------------------------------------
# Default constructor mein fixed (hardcoded) values di jati hain.

class StudentDefault:
    def __init__(self):
        self.name = "Ishfaq Khan"
        self.age = 20

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

print("2.1 Default Constructor")
s1 = StudentDefault()
s1.show()
print("-" * 60)


# ---------------------------------------------------------------------
# 2.2 Parameterized Constructor
# ---------------------------------------------------------------------
# Parameterized constructor mein values object banate waqt di jati hain,
# har object ki apni alag values ho sakti hain.

class StudentParam:
    def __init__(self, name, age, roll):
        self.name = name
        self.age = age
        self.roll = roll

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll}")

print("2.2 Parameterized Constructor")
s1 = StudentParam("Ishfaq Wazir", 20, 2332)
s2 = StudentParam("Hassan", 20, 4434)
s1.show()
s2.show()
print("-" * 60)


# ---------------------------------------------------------------------
# 2.3 Mini Project: Car Details using Constructor
# ---------------------------------------------------------------------

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)

print("2.3 Mini Project — Car Details")
car1 = Car(brand="Corolla", model="2024", price=6500000)
car1.show_details()
print("-" * 60)


# =====================================================================
# 3. ENCAPSULATION
# =====================================================================
# Encapsulation ka matlab hai data ko "wrap" karke protect karna —
# yani important data ko bahar se direct access na hone dena, sirf
# methods ke through access dena.

# ---------------------------------------------------------------------
# 3.1 Public Variable — har jagah se access ho sakta hai
# ---------------------------------------------------------------------
class StudentPublic:
    def __init__(self):
        self.name = "Ali"   # Public variable

print("3.1 Public Variable")
s = StudentPublic()
print(s.name)   # Bahar se direct access ho gaya
print("-" * 60)


# ---------------------------------------------------------------------
# 3.2 Protected Variable — sirf class aur uski subclasses ke liye
#     (single underscore _ se banta hai — ye sirf ek convention hai)
# ---------------------------------------------------------------------
class StudentProtected:
    def __init__(self):
        self._age = 20   # Protected variable

print("3.2 Protected Variable")
s = StudentProtected()
print(s._age)   # Access ho sakta hai, lekin convention yahi hai ke bahar se na kiya jaye
print("-" * 60)


# ---------------------------------------------------------------------
# 3.3 Private Variable — sirf usi class ke andar access hota hai
#     (double underscore __ se banta hai)
# ---------------------------------------------------------------------
class StudentPrivate:
    def __init__(self):
        self.__marks = 90   # Private variable

    def show_marks(self):
        print(self.__marks)

print("3.3 Private Variable")
s = StudentPrivate()
s.show_marks()
# print(s.__marks)   # Ye line error degi, kyunke __marks private hai
print("-" * 60)


# ---------------------------------------------------------------------
# 3.4 Assignment: Bank Account System using Encapsulation
# ---------------------------------------------------------------------
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private, direct change nahi ho sakta

    def show_balance(self):
        print("Balance:", self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(amount, "Rs Deposit Ho Gaye")
        else:
            print("Amount sahi nahi hai")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(amount, "Rs Withdraw Ho Gaye")
        else:
            print("Aap ke account mein itna balance nahi hai")

print("3.4 Mini Project — Bank Account System")
account = BankAccount("Ishfaq Khan", 50000)
account.show_balance()
account.deposit(6000)
account.show_balance()
account.withdraw(26000)
account.show_balance()
print("-" * 60)


# =====================================================================
# 4. INHERITANCE
# =====================================================================
# Inheritance ka matlab hai ek class (Child) dusri class (Parent) ki
# properties aur methods use kar sakti hai — bina dobara likhe.

# ---------------------------------------------------------------------
# 4.1 Single Inheritance
# ---------------------------------------------------------------------
class Vehicle:
    def start(self):
        print("Vehicle is starting!")

class CarSingle(Vehicle):
    def drive(self):
        print("Vehicle is running!")

print("4.1 Single Inheritance")
c1 = CarSingle()
c1.start()   # Parent class ka method
c1.drive()   # Child class ka apna method
print("-" * 60)


# ---------------------------------------------------------------------
# 4.2 Multilevel Inheritance (Parent -> Child -> Grandchild)
# ---------------------------------------------------------------------
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Puppy(Dog):
    def weep(self):
        print("Puppy is weeping")

print("4.2 Multilevel Inheritance")
p = Puppy()
p.eat()    # Animal se
p.bark()   # Dog se
p.weep()   # apna
print("-" * 60)


# ---------------------------------------------------------------------
# 4.3 Multiple Inheritance (ek class do parents se inherit karti hai)
# ---------------------------------------------------------------------
class Father:
    def skills(self):
        print("Father: Business")

class Mother:
    def hobby(self):
        print("Mother: Painting")

class Child(Father, Mother):
    pass

print("4.3 Multiple Inheritance")
ch = Child()
ch.skills()
ch.hobby()
print("-" * 60)


# ---------------------------------------------------------------------
# 4.4 Hierarchical Inheritance (ek Parent se kai Child classes)
# ---------------------------------------------------------------------
class Shape:
    def info(self):
        print("This is a shape")

class Circle(Shape):
    def area(self, r):
        print("Circle Area:", 3.14 * r * r)

class Square(Shape):
    def area(self, side):
        print("Square Area:", side * side)

print("4.4 Hierarchical Inheritance")
circle = Circle()
square = Square()
circle.info()
circle.area(5)
square.info()
square.area(4)
print("-" * 60)


# ---------------------------------------------------------------------
# 4.5 super() — Parent class ka constructor/method call karne ke liye
# ---------------------------------------------------------------------
class Person:
    def __init__(self, name):
        self.name = name
        print("Person Constructor Called")

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)   # Parent ka constructor call kiya
        self.salary = salary
        print("Employee Constructor Called")

    def show(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

print("4.5 super() Example")
e1 = Employee("Ishfaq Khan", 50000)
e1.show()
print("-" * 60)


# =====================================================================
# 5. POLYMORPHISM
# =====================================================================
# Polymorphism ka matlab hai "ek naam, alag-alag forms/behavior".

# ---------------------------------------------------------------------
# 5.1 Method Overriding — Child class Parent ke method ko apne
#     hisaab se dobara define karti hai
# ---------------------------------------------------------------------
class Bird:
    def sound(self):
        print("Birds make sound")

class Parrot(Bird):
    def sound(self):
        print("Parrot says: Hello!")

class Crow(Bird):
    def sound(self):
        print("Crow says: Caw Caw!")

print("5.1 Method Overriding")
for bird in (Parrot(), Crow(), Bird()):
    bird.sound()   # Har object apna sound() call karega
print("-" * 60)


# ---------------------------------------------------------------------
# 5.2 Method Overloading (Python mein default arguments se hota hai)
# ---------------------------------------------------------------------
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

print("5.2 Method Overloading (via default args)")
calc = Calculator()
print("2 numbers:", calc.add(5, 10))
print("3 numbers:", calc.add(5, 10, 15))
print("-" * 60)


# ---------------------------------------------------------------------
# 5.3 Operator Overloading — operators (+, -, etc.) ko apni classes
#     ke liye customize karna
# ---------------------------------------------------------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):   # + operator ka custom behavior
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):          # print() karte waqt kya dikhega
        return f"({self.x}, {self.y})"

print("5.3 Operator Overloading")
p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2   # yahan __add__ automatically call hoga
print("Result Point:", p3)
print("-" * 60)


# =====================================================================
# 6. ABSTRACTION
# =====================================================================
# Abstraction ka matlab hai sirf zaroori cheezein dikhana, andar ka
# complex implementation chupa dena. Python mein ye ABC (Abstract
# Base Class) se karte hain.

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass   # Sirf structure diya, implementation force ki child pe

class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Card")

class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Cash")

print("6. Abstraction")
# PaymentMethod()   # Ye error dega, abstract class ka object nahi ban sakta
p1 = CardPayment()
p2 = CashPayment()
p1.pay(1500)
p2.pay(500)
print("-" * 60)


# =====================================================================
# 7. CLASS VARIABLES vs INSTANCE VARIABLES
# =====================================================================
# Class variable: saare objects ke beech SHARE hota hai
# Instance variable: har object ka apna alag hota hai

class Counter:
    total_objects = 0   # Class variable (shared)

    def __init__(self, name):
        self.name = name          # Instance variable (unique per object)
        Counter.total_objects += 1

print("7. Class vs Instance Variables")
c1 = Counter("First")
c2 = Counter("Second")
c3 = Counter("Third")
print("Total objects created:", Counter.total_objects)
print("-" * 60)


# =====================================================================
# 8. CLASS METHOD & STATIC METHOD
# =====================================================================
class MathTools:
    school_name = "Axis Institute"

    def __init__(self, value):
        self.value = value

    def instance_method(self):
        print("Instance method, value:", self.value)

    @classmethod
    def change_school(cls, new_name):   # cls -> class ko refer karta hai
        cls.school_name = new_name
        print("School name changed to:", cls.school_name)

    @staticmethod
    def add(a, b):   # self/cls ki zaroorat nahi, simple utility function
        return a + b

print("8. Class Method & Static Method")
MathTools.change_school("Tech Prime Academy")
print("Static method result:", MathTools.add(10, 20))
print("-" * 60)


# =====================================================================
# 9. GETTER / SETTER using @property
# =====================================================================
# @property se hum kisi private variable ko safely read/write karne
# dete hain, lekin beech mein validation bhi laga sakte hain.

class Employee2:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):        # Getter
        return self.__salary

    @salary.setter
    def salary(self, value):  # Setter (validation ke sath)
        if value < 0:
            print("Salary negative nahi ho sakti!")
        else:
            self.__salary = value

print("9. Getter/Setter using @property")
emp = Employee2(50000)
print("Current salary:", emp.salary)
emp.salary = 60000     # setter call hoga
print("Updated salary:", emp.salary)
emp.salary = -500      # invalid, validation rok degi
print("-" * 60)


# =====================================================================
# 10. DUNDER (MAGIC) METHODS — __str__, __len__, __repr__
# =====================================================================
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):     # print(object) karte waqt ye chalega
        return f"Book: {self.title}"

    def __len__(self):     # len(object) karte waqt ye chalega
        return self.pages

print("10. Dunder Methods")
b1 = Book("Python Basics", 250)
print(b1)          # __str__ call hoga
print(len(b1))     # __len__ call hoga
print("-" * 60)


# =====================================================================
# 11. COMPOSITION (Has-A Relationship)
# =====================================================================
# Inheritance "IS-A" relationship banata hai (Car IS-A Vehicle),
# Composition "HAS-A" relationship banata hai (Car HAS-A Engine).

class Engine:
    def start(self):
        print("Engine started")

class Car2:
    def __init__(self):
        self.engine = Engine()   # Car ke andar Engine ka object hai

    def start_car(self):
        self.engine.start()      # Engine ka method use kar rahe hain
        print("Car is ready to drive")

print("11. Composition")
car2 = Car2()
car2.start_car()
print("-" * 60)


# =====================================================================
# 12. FINAL MINI PROJECT — Library Management (Sab concepts mila kar)
# =====================================================================
class LibraryItem(ABC):
    def __init__(self, title):
        self.title = title
        self._is_borrowed = False   # protected

    @abstractmethod
    def item_type(self):
        pass

    def borrow(self):
        if not self._is_borrowed:
            self._is_borrowed = True
            print(f"'{self.title}' borrowed successfully.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def __str__(self):
        status = "Borrowed" if self._is_borrowed else "Available"
        return f"{self.item_type()}: {self.title} [{status}]"


class LibraryBook(LibraryItem):
    def item_type(self):
        return "Book"


class Magazine(LibraryItem):
    def item_type(self):
        return "Magazine"


print("12. Final Mini Project — Library Management System")
items = [
    LibraryBook("Learning Python"),
    Magazine("AI Weekly"),
]

for item in items:
    print(item)

items[0].borrow()
items[0].borrow()   # dobara try karega -> already borrowed message
print(items[0])
print("-" * 60)

print("Done! Ye file OOP ke saare basic se advanced concepts cover karti hai.")
