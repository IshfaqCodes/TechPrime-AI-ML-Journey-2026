#----<<<<<<<Loops>>>>>>>----
#--<<For loop>>--
#Without Loop
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")


#With Loop
for i in range(5):
    print("Welcome!")
    
#Even numbers  
for i in range(1,20,-1):
    if i%2==0:
        print(i)
        
#Odd numbers  
for i in range(1,20,-1):
    if i%2!=0:
        print(i)
        
#Multiplication
number=int(input("please enter the number= "))
for i in range(1,10):
    print(number,"x",i,"=",number*i)
    #print(f"{number} x {i} ={number*i}")  2nd method

#range(Start, Stop, Step)
for i in range(0,11,2):
    print(i)

#for Loop on List
fruits=["Apple","Banana","Orange"]

for fruit in fruits:
    print(fruit)

#Nested Loop
for table in range(1,4):
    print("Table of", table)

    for i in range(1,11):
        print(table, "x", i, "=", table*i)

    print()

#Stars 3 row 4 colmn using Nested Loop
for row in range(3):
    for col in range(4):
        print("*", end=" ")
    print()
    
    

#<<>>------While Loop------<<>>>
#count =int(input("Please enter the count= "))
count=1
while count <= 5:
    print(count)
    count += 1

#Passwerd cheker using while loop
paswerd=1234
user=0
while user!=paswerd:
    user=int(input("plese enter your paswerd="))
    if user!=paswerd:
           print("I am sorry your passwerd is incorrect!")
print("Login Successful")  

#Finding the number using while loop
num=54
while num==54:
    Guess=int(input("Plese Guess the Number= "))
    if Guess==num:
        print("Congratulations! you are right")
        break  #to stop
    else:
        print("Try Again!")
        

#----->>>Functions<<<<---
#How to creat a function 
def student():
    print("I am ishfaq khan")
student() #print 1 time
student() #print 2 time

 
def student(name, age):
    print(name)
    print(age)

student("Ishfaq",21)

#------Function best simple project for understanding-------

#Function for Addition 
def add(a, b):
    return a + b

#Function for Subtraction 
def subtract(a, b):
    return a - b

# Function for Multiplication 
def multiply(a, b):
    return a * b

# Function for Division 
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b


#inpute from user
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("\nChoose Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter Choice (1-4): ")

if choice == "1":
    print("Result =", add(num1, num2))

elif choice == "2":
    print("Result =", subtract(num1, num2))

elif choice == "3":
    print("Result =", multiply(num1, num2))

elif choice == "4":
    print("Result =", divide(num1, num2))

else:
    print("Invalid Choice!")



#  ----------In simple-----------
# Function
def add(a, b):
    print("Answer =", a + b)

# Input
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

# Function Call
add(num1, num2)

