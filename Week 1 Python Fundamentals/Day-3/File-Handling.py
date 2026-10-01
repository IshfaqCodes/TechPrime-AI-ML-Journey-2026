#To open file 
file1=open('ai-ml-internship/Week 1 Python Fundamentals/Day-3/text file.txt',"r")
#To read file
data=file1.read()
#To print the file 
print("Data od the file is =",data)

lowerdata=data.lower()
word=input("please search a word in data= ")

if word.lower() in lowerdata:
    print("Yes ishfaq khan is present in data")
else:
    print("not present in data")
    

#with open
with open("data.txt", "r") as file:
    print(file.read())


#read line by line
file = open("data.txt", "r")
print(file.readline())
print(file.readline())
file.close()

#readlines
file = open("data.txt", "r")
lines = file.readlines()
print(lines)
file.close()



#wright mood 
file2=open('ai-ml-internship/Week 1 Python Fundamentals/Day-3/text file.txt',"w")
file2.write("mera name ishfaq hay awer main bs AI ka student from bannu university")


#Appand mood
file3=open('ai-ml-internship/Week 1 Python Fundamentals/Day-3/text file.txt',"a")
file3.write("so i want to learn ai and machin learning.")

#Create a new file if file 
file3=open('ai-ml-internship/Week 1 Python Fundamentals/Day-3/text new file.txt',"x")
file3.write("this is new fileok bro")

#Rename the file 
import os

os.rename("ai-ml-internship/Week 1 Python Fundamentals/Day-3/text new file.txt","new file.txt")



#Remove
os.remove("ai-ml-internship/Week 1 Python Fundamentals/Day-3/new file.txt")