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
x=int(input("enter your first number"))
y=int(input("enter your second number"))
if x>y:
    print("x is greater than y")
else:
    print("y is greater")
Q=11
marks=90
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
Q=12
number=45
if number>15:
    print("positive")
elif number<-15:
    print("negitive")
else:
    print("zero")

Q=13
num=int(input("1 monday 2 tuseday 3 wednesday 4 thursday 5 friday"))
if num==1:
    print("M")
elif num==2:
    print("T")
elif num==3:
    print("W")
elif num==4:
    print("TH")
elif num==5:
    print("F")
else:
    print("koi na")

Q=14
marks=int(input("marks in enter here"))
if marks>=99:
    print("Excellent")
elif 85<marks<90:
    print("Good")
elif 40<marks<75:
    print("Pass")
else:
    print("fail")
Q=15
number=int(input("enter in number"))
if number==0:
    print("1")
elif number==1:
    print("2")
elif number==3:
    print("3")
else:
   print("other")





Q=16
first =int(input("enter in first in number"))
if first>=45:
    if first<=60:
      print("Between 18 and 60")
    else:
      print("none")
else:
   print("kuch nai")

#Q=17
marks=int(input("student in passed marks"))
if marks >=40:
    if marks>=75:
     print("Good")
    else:
       print("passed")
else:
    print("Failed")

Q=18
number=int(input("enter in positive value"))
if number>10:
    if number>100:
        print("grater than 100")
    else:
        print("positive value")
else:
    print("is positive in value")

 Q=19
age=int(input("enter in age "))
if age>=18:
    if age>=60:
        print("hopeless")
    else:
        print("unope")
else:
    print("click")

Q=20
a=int(input("number in paste in p and np"))
if a>=0:
    if a<=0:
      print("positive")
    else:
       print("number")
else:
   print("negative")

Q=21
age=int(input("enter your age:"))
marks=int (input("enter your marks:"))
if age>=18 and marks>=40:
    print("Eligible")
else:
    print("Not Eligible")  
Q=22
number=int(input("enter your number:"))
if number<10 or number>100:
    print("Special")
else:
    print("not special")

Q=23
age=int(input("enter in age:"))
has_id=bool(input("enter in boolean:"))
if age >= 18 and has_id is True:
    print("Allowed")
else:
    print("not allowed")
Q=24
first_number=int(input("enter your first number"))
second_number=int(input("enter your second number"))
if first_number > 10 and second_number > 10:
    print("Both are greater than 10")
else:
    print("not")

Q=25
a=int(input("enter your number:"))
if a<0 or a>100:
    print("right")
else:
    print("rong")

Q=26
is_closed = False
if not is_closed:
    print("open")
Q=27
number=int(input("enter your number"))
if number>=10 and number<=50:
    print("TRUE")
else:
    print("FALSE")
Q=28
number=int(input("enter your number:"))
if number>=10 or number>=50:
  print("right") 
else:
  print("not right")
Q=29
is_student=True
has_id=True
has_ticket=True
if is_student==True and has_id==True and has_ticket==True:
    print("Allowed")
else:
    print("Not Allowed")  
Q=30
age=int(input("enter your age"))
marks=int(input("enter your marks"))
has_id=True
if age>=18 and marks>40 and has_id==True:
    print("eligible")
else:
    print("not eligible")

