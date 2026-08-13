#Task 1: Student Information Program
import re


print("Welcome to the Student info program")
Name = input("Enter your Name:")
College_Name = input("Enter your college name:")
Branch = input("Enter your branch:")
print("\n-----Student Information-----")
print(f"Name         : {Name}")
print(f"College Name : {College_Name}")
print(f"Branch       : {Branch}")

#Task 2: Print each variable along with its data type using type().
a=5
b=5.5
c="Hello"
d=True
print("\n-----Variable Data Types-----")
print("Data Type of", a ," is:",type(a))
print("Data Type of", b ," is:",type(b))
print("Data Type of", c ," is:",type(c))
print("Data Type of", d ," is:",type(d))

#Task 3: Create a calculator program that performs:
Num_1 = int(input("\nEnter the first number:"))
Num_2 = int(input("Enter the second number:"))
Addition = Num_1 + Num_2
Subraction = Num_1 - Num_2
Multiplication = Num_1 * Num_2
if Num_2 != 0:
    Division = Num_1 / Num_2
    Module = Num_1 % Num_2
else:
 Division = "Undefined (cannot divide by zero)"
 Module = "Undefined (cannot divide by zero)"
print("\n----- Calculator Results-----")
print(f"Addition: {Num_1} + {Num_2} = {Addition}")
print(f"Subtraction: {Num_1} - {Num_2} = {Subraction}")
print(f"Multiplication: {Num_1} * {Num_2} = {Multiplication}")
print(f"Division: {Num_1} / {Num_2} = {Division}")
print(f"Modulus: {Num_1} % {Num_2} = {Module}")

# Task 4: Displays the grade using if, elif, and else.
Marks = int(input("Enter the sub_1 mark:   "))
if Marks >= 90:
    print("A grade")
elif Marks >= 75:
    print("B grade")
elif Marks >= 60:
     print("C grade")
else:
    print("Fail")
#For overall Grade
Sub_1 = int(input("Enter the sub_1 mark:   "))
Sub_2 = int(input("enter the sub_2 mark:   "))
Sub_3 = int(input("enter the sub_3 mark:   "))
Sub_4 = int(input("enter the sub_4 mark:   "))
Sub_5 = int(input("enter the sub_5 mark:   "))
Avg = (Sub_1 + Sub_2 + Sub_3 + Sub_4 + Sub_5) / 5
if Avg >= 90:
    print("A grade")
elif Avg >= 75:
    print("B grade")
elif Avg >= 60:
     print("C grade")
else:
    print("Fail")

#Task 5: Print numbers from 1 to 20 using a for loop.
for i in range(1, 21):
    print("\n",i)

#Print the multiplication table of any number.
num = int(input("Enter a number: "))
n= int(input("Enter a number: "))
for i in range(1,n):
    print(num, "x", i, "=", num * i)

#Print even numbers from 1 to 50 using a while loop.
n = 2
while n<=50:
 print("\n",n)
 n += 2

#Task 6: Function to calculate the square of a number.
n=int(input("Enter the number:   "))
def sqt(n):
    return n **2
result=sqt(n)
print(result)

#Function to calculate the average of three numbers.
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))
def average(a, b, c):
    return (a + b + c) / 3
print("Average:", average(x, y, z))

#Task 7 Strings & Collections 
#String operations (upper(), lower(), replace(), find())
word=input("Enter a word: ")
replace = input("Enter the text to replace: ")
placed = input("Enter the text to place: ")
search = input("Enter the text to find: ")
print(word.upper())
print(word.lower())
print(word.replace(replace, placed))
print(word.find(search))

#List operations (append(), remove(), sort())
w = []
w_1 = input("Enter a word: ")
w_2 = input("Enter a word: ")
w_3 = input("Enter a word: ")
w.append(w_1)
w.append(w_2)
w.append(w_3)
print("\nOriginal list:",w)
append_word = input("Enter a word to append: ")
w.append(append_word)
print("Appended word:", w)
remove_word = input("Enter a word to remove: ")
w.remove(remove_word)
print("After removal:", w)
w.sort()
print("Sorted list:", w)
#Tuple creation and indexing
t=()
t_1 =input("Enter the first value:  ")
t_2 =input("Enter the second value:  ")
t_3 =input("Enter the third value:  ")
t_4 =input("Enter the fourth value:  ")
t=(t_1,t_2,t_3,t_4)
print ("\n",t)
print(t[0])
print(t[1])
print(t[2])
print(t[3])
