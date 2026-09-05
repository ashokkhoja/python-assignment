#Q=1
x=18
if x>12:
    print("Greater than 10")
#Q=2
age=18
if age>=18:
    print("Adult")
#Q=3
a=int(input("positive number"))
if a>0:
    print("enter positive number in")
#Q=4
marks=40
if marks>=40:
    print("pass")
#Q=5
num=int(input("enter number"))
if num==0:
    print("zero")

#Q=6
num=int(input("enter an number"))
if num>=0:
    print("positive")
else:
    print("negitive")

#Q=7
age=int(input("enter your age:-"))
if age>=18:
    print("Adult")
else:
    print("minor")


#Q=8
x=int(input("enter an number:-"))
if x%2==0:
    print("enter number is even")
else:
    print("enter number is odd")


#Q=9
marks=int(input("enter your marks"))
if marks>=40:
    print("pass")
else:
    print("fail")


#Q=10
x=int(input("enter your first number:-"))
y=int(input("enter your second number:-"))
if x>y:
    print("x is greater than y")
else:
    print("y is greater")

#Q=11
marks=int(input("enter your marks:-"))
if marks>=90:
    print("A")
elif 75<marks<89:
    print("B")
elif 60<marks<74:
    print("C")
elif 40<marks<59:
    print("D")
else:
    print("F")

#Q=12
num=int(input("enter an number:-"))
if num>0:
    print("enter number is positive")
elif num==0:
    print("enter number is zero")
else:
    print("enter number is negitive")

#Q=13
a=int(input("enter your choise:-"))
if a==1:
    print("Monday")
elif a==2:
    print("Tuesday")
elif a==3:
    print("Wednesday")
elif a==4:
    print("Thursday")
elif a==5:
    print("Friday")
else:
    print("other")

#Q=14
marks=int(input("enter your marks:-"))
if marks>=90:
    print("Excellent")
elif 60<marks<89:
    print("Good")
elif 40<marks<59:
    print("Pass")
else:
    print("Fail")

#Q=15
a=int(input("enter your choise:-"))
if a==1:
    print("1")
elif a==2:
    print("2")
elif a==3:
    print("3")
else:
    print("other")

#Q=16
age=int(input("enter your age:-"))
if age>=18:
    if age<=60:
        print("Between 18 and 60")
    else:
        print("greatre than 60")
else:
    print("minor")

#Q=17
marks=int(input("enter your marks:-"))
if marks>=40:
    if marks>=75:
        print("Good")
    else:
        print("pass")
else:
    print("failed")

#Q=18
a=int(input("Enter your number:-"))
if a>0:
    if a>100:
        print("Number is greatre than 100")
    else:
        print("Positive but less than 100")
else:
    print("zero or negative")


#Q=19
age=int(input("enter your age:-"))
if age>=18:
    if age<=60:
        print("Between 18 and 60")
    else:
        print("greatre than 60")
else:
    print("minor")

#Q=20
num = int(input("Enter a number: "))
if num != 0:
    if num > 0:
        print("The number is positive.")
    else:
        print("The number is negative.")
else:
    print("The number is zero.")
    #Q=21
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

if age >= 18 and marks >= 40:
    print("Eligible")
#Q=22
number = float(input("Enter a number: "))

if number < 10 or number > 100:
    print("Special")
#Q=23
age = int(input("Enter age: "))
has_id = input("Do you have ID? (true/false): ").strip().lower() == "true"

if age >= 18 and has_id:
    print("Allowed")
#Q=24
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > 10 and num2 > 10:
    print("Both are greater than 10")
#Q=25
number = float(input("Enter a number: "))

if number < 0 or number > 100:
    print("Out of range")
#Q=26
is_closed = False

if not is_closed:
    print("Open")
#Q=27
number = float(input("Enter a number: "))

if number >= 10 and number <= 50:
    print("Number is between 10 and 50")
#Q=28
number = float(input("Enter a number: "))

if number < 10 or number > 50:
    print("Number is outside the range 10 to 50")
#Q=29
is_student = True
has_id = True
has_ticket = True

if is_student and has_id and has_ticket:
    print("Allowed")
#Q=30
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
has_id = input("Do you have ID? (true/false): ").strip().lower() == "true"

if age >= 18 and marks >= 40 and has_id:
    print("Eligible")
else:
    print("Not eligible")