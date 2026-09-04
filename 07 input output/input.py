#Q=1
name=input("Enter your name:")
print("your name is:",name)

#Q=2
city=input("Enter your city:")
print("Your city is",city)

#Q=3
user_name=input("Enter your namr:")
user_age=int(input("Enter your age"))
print(user_name)
print(user_age)

#Q=4
print(type(input()))

#Q=5
a=input("Enter your name:")
print(type(a))

#Q=6
fname=input("Enter your first name:")
lname=input("Enter your last name:")
print("your full name is:",fname+lname)

#Q=7
name=input("Enter your name:")
city=input("Enter your city:")
college=input("Enter your college:")
print(name)
print(city)
print(college)

#Q=8
fname,lname=input("Enter your full name:").split()
print(fname)
print(lname)

#Q=9
fvariable,svariable=input("Enter Python Programming:").split()
print(fvariable)
print(svariable)

#Q=10
a,b,c=input("Enter three words:").split()
print(a)
print(b)
print(c)

#Q=11
a="25"
a=int(a)
print(a,type(a))

#Q=12
a="25.5"
a=float(a)
print(a,type(a))

#Q=13
a=100
a=str(a)
print(a,type(a))

#Q=14
num=int(input("Enter your num"))
num=str(num)
print(num,type(num))

#Q=15
num=float(input("Enter your num"))
num=str(num)
print(num,type(num))

#Q=16
fname=input("Enter your first name:")
lname=input("Enter your last name:")
print(fname+lname)
print("beacause python takes input value by default in string")

#Q=17

num1=(input("Enter your num1"))
num2=(input("Enter your num2"))
num1=int(num1)
num2=int(num2)
print(num1+num2)

#Q=18
name = "Rahul"
age = 20
print(f"My name is {name} and I am {age} years old.")

#Q=19
a = 10
b = 20
print(f"sum is{a+b}")

#Q=20
user_name=input("Enter your namr:")
user_age=int(input("Enter your age"))
print(f"My name is {user_name} and I am {user_age} years old.")

#Q=21
product_price=float(input("Enter product price:"))
print(f"{product_price:.2f}")

#Q=23
product_name=input("Enter product name:")
product_price=float(input("Enter product price:"))
product_quantity=int(input("Enter product quantity:"))
print(f"my favourite product is {product_name} and i will buy {product_quantity} paying {product_price} of each")

#Q=24

print("A", "B", "C")

#Q=25
print("2026", "08", "19",sep="-")

#Q=26
print("Hello",end=" ")
print("World")

#Q=27
num1=(input("Enter your num1"))
num2=(input("Enter your num2"))
print(f"sum {num1+num2}")

#Q=28
product_price=float(input("Enter product price:"))
product_quantity=int(input("Enter product quantity:"))
print(f"total cost {product_price*product_quantity}")

#Q=29
name=input("Enter your name:")
age=int(input("Enter your age:"))
marks=float(input("Enter your marks:"))
print(f"my name is {name} and i am {age} years old and i will get {marks}% marks in class 10")

#Q=30
student_name=input("Enter student name:-")
age=int(input("Enter your age:-"))
height=float(input("enter your height:-"))
city=input("Enter your city:-")
print(f"My name is {student_name} and My age is {age} and my height is {height:.2f} and i am from {city}")