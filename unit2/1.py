dbms = int(input("Enter marks for DBMS: "))
python = int(input("Enter marks for Python: "))
ai = int(input("Enter marks for AI: "))
maths = int(input("Enter marks for Maths: "))

total = dbms + python + ai + maths
per = total / 400 * 100

if dbms >= 40 and python >= 40 and ai >= 40 and maths >= 40:
    print("Passed in each subject.")
else:
    print("You are fail.")

if per >= 90:
    print("Grade: Distinction")
elif per >= 75:
    print("Grade: First Class")
elif per >= 50:
    print("Grade: Second Class")
elif per >= 40:
    print("Grade: Pass Class")
else:
    print("Grade: Fail")
