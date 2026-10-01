# Example of variable
x = 5 
y = "Ishfaq Khan"
print(x) 
print(y) 


name=input("please enter your name=")
age=int(input("plese enter your age="))
print(type(name))
print(type(age))


#Data Types....................

#---<<Basics Types>>---
#int
a=23  
print(type(a))

#float
x = 3.14
print(x)
print(type(x))

#complex
x = 4 + 3j
print(x)
print(type(x))

#Boolean
x = True
print(x)
print(type(x))

#------------------String----------------------------
x = "This is IK"
print(x)
print(type(x))

#----String Operations----

#<<Concatenation>>
first_name = "Ishfaq"
last_name = "Khan"
print(first_name + " " + last_name)


#<<Repetition>>
text = "I am hassan"
print(text * 3)

#<<Find Length>>
text = "Jamshid"
print(len(text))

#---------String Formatting--------
#Using + add two strings
name = "Ali"
print("Hello " + name)

#Using f-string
name = "Sajid"
age = 26
print(f"My name is {name} and I am {age} years old.")

#Using .format()
name = "Wasif"
print("Welcome {}".format(name))


#-----String Modification--------
#upper()
text = "ishfaq khan is a ai student"
print(text.upper())

#lower()
text = "ishfaq khan is a ai student"
print(text.lower())

#replace()
text = "I like coding"
print(text.replace("coding", "Python"))

#strip()
text = "  Ik  "
print(text.strip())

#split()
text = "i am ishfaq from bannu"
print(text.split())



#---------------------=========<<<<<<<Container Type>>>>============....--------------------

#List
Students = ["Ishfaq", "Faisal", "Hamad"]
print(Students)
print(type(Students))

#Tuple
numbers = (10, 20, 30)
print(numbers)
print(type(numbers))

#Dec
student = {"Name": "Ishfaq Khan", "Age": 20}
print(student)
print(type(student))

#Set
colors = {"Red", "Green", "Blue"}
print(colors)
print(type(colors))



#Dynamic Typing....
x = 5
print(type(x))

x = "Hello"
print(type(x))

#Multiple Variable Assignment
a, b, c = 1, 2, 3
print(a, b, c)

#Same Value Assignment
x = y = z = 100
print(x, y, z)


