#Task 1: Student Information Program
print("Welcome to the Student info program")
Name = input("Enter your Name: ")
College_Name = input("Enter your college name: ")
Branch = input("Enter your branch: ")
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
Num_1 = int(input("\nEnter the first number:  "))
Num_2 = int(input("Enter the second number: "))
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
Marks = int(input("\nEnter the sub_1 mark:   "))
if Marks >= 90:
    print("A grade")
elif Marks >= 75:
    print("B grade")
elif Marks >= 60:
     print("C grade")
else:
    print("Fail")
#For overall Grade
Sub_1 = int(input("\nEnter the sub_1 mark:   "))
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
print("\nNumbers from 1 to 20: ")
for i in range(1, 21):
     print(i)

#Print the multiplication table of any number.
num = int(input("\nEnter a number: "))
n= int(input("Enter a number: "))
for i in range(1,n):
    print(num, "x", i, "=", num * i)

#Print even numbers from 1 to 50 using a while loop.
n = 2
print("\nEven numbers from 1 to 50: ")
while n<=50:
 print(n)
 n += 2

#Task 6: Function to calculate the square of a number.
n=int(input("\nEnter the number:   "))
def sqt(n):
    return n **2
result=sqt(n)
print(result)

#Function to calculate the average of three numbers.
x = float(input("\nEnter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))
def average(a, b, c):
    return (a + b + c) / 3
print("Average:", average(x, y, z))

#Task 7 Strings & Collections 
#String operations (upper(), lower(), replace(), find())
word=input("\nEnter a word: ")
replace = input("Enter the text to replace: ")
placed = input("Enter the text to place: ")
search = input("Enter the text to find: ")
print(word.upper())
print(word.lower())
print(word.replace(replace, placed))
print(word.find(search))

#List operations (append(), remove(), sort())
w = []
w_1 = input("\nEnter a word: ")
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
t_1 =input("\nEnter the first value:  ")
t_2 =input("Enter the second value:  ")
t_3 =input("Enter the third value:  ")
t_4 =input("Enter the fourth value:  ")
t=(t_1,t_2,t_3,t_4)
print ("\n",t)
print("\nThis is index 0 value",t[0])
print("This is index 1 value",t[1])
print("This is index 2 value",t[2])
print("This is index 3 value",t[3])

#Dictionary storing student information
student={}
student["roll_no"] = int(input("\nEnter roll number: "))
student["name"] = input("Enter student name: ")
student["age"] = int(input("Enter age: "))
student["course"] = input("Enter course: ")
student["marks"] = float(input("Enter marks: "))
print("\nStudent information", student)
print("Roll No:", student["roll_no"] )
print("Name:", student["name"] )
print("Age:", student["age"] )
print("Course:", student["course"] )
print("Marks:", student["marks"] )  
student["course"] = input("Enter new one: ")
print("Updated:", student)

#Set operations (add(), remove())
s={}
s_1 = input("\nEnter the value: ")
s_2 = input("Enter the value: ")
s_3 = input("Enter the value: ")
s={s_1,s_2,s_3}
print("\nOriginal set:",s)
s.add(input("Enter a value to add: "))
print("After adding:", s)
s.remove(input("Enter a value to remove: "))
print("After removing:", s)

#Task 8: Creates,reads & display a text file
introduction = " Hi, my name is Kalpana." 
"I am a Computer Science graduated with a passion for programming and problem-solving." 
"I enjoy learning new technologies and building projects that solve real-world problems." 
"In my free time, I like to do coding & learning."
with open("introduction.txt","w")as f:
 f.write(introduction)
 print("\nIntroduction has been written to 'introduction.txt'\n")
with open("introduction.txt","r")as f:
 f.read()
print("Displaying the content: ", introduction)

#Task 9: Student Record Management System
students = [] 
def add_student():
    name = input("\nEnter student name: ").strip()
    age = input("Enter student age: ").strip()
    major = input("Enter student major: ").strip()
    student = {
        "name": name,
        "age": age,
        "major": major}
    students.append(student)
    print(f"\n Student '{name}' added successfully!\n")
def display_students():
    if not students:
        print("\n No student records found.")
        return
    print("\n" + "=" * 40)
    print("ALL STUDENT RECORDS")
    print("=" * 40)
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, "
              f"Age: {student['age']}, "
              f"Major: {student['major']}")
    print("=" * 40 + "\n")
def search_student():
    name = input("Enter the name to search: ").strip().lower()
    found = [s for s in students if s["name"].lower() == name]
    if found:
        print("\n Student found:")
        for s in found:
            print(f"Name: {s['name']}, Age: {s['age']}, Major: {s['major']}\n")
    else:
        print(f"\n No student found with the name '{name}'.\n")
def delete_student():
    name = input("Enter the name of the student to delete: ").strip().lower()
    for s in students:
        if s["name"].lower() == name:
            students.remove(s)
            print(f"\n Student '{s['name']}' deleted successfully!\n")
            return
    print(f"\n No student found with the name '{name}'.\n")
def menu():
    """Display menu and handle user choices."""
    while True:
        print("\n STUDENT RECORD MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by Name")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("\n Enter your choice (1-5): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("\n Exiting the system. Goodbye!")
            break
        else:
            print("\n Invalid choice. Please enter a number between 1 and 5.\n")
if __name__ == "__main__":
    menu() 




