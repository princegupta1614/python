#9. Write a program to define and use user-defined functions with different types of arguments. 
def stud(name, age, per):
    print("Name: ", name)
    print("Age: ", age)
    print("Percentage: ", per)

name = input("Enter student name: ")
age = int(input("Enter age: "))
per = input("Enter Percentage: ")
stud(name, age, per)
