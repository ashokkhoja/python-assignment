# Part A — Intermediate Problems

# Q=1

# marks = int(input("Enter marks: "))
# while marks < 0 or marks > 100:
#     marks = int(input("Enter valid marks: "))
# print("Accepted marks:", marks)

# Q=2

# number=int(input("enter in numbers:"))
# while number<=0:
#     number=int(input("enter in  numbers:"))
# print("Accepted number:",number)


# Q=3

# age=int(input("enter in your age:"))
# while age<0 or age>120:
#     age=int(input("enter in your correct age:"))
# print("Accept age:",age)


# Q=4


# while True:
#     print("1. View profile")
#     print("2. Edit profile")
#     print("3. Settings")
#     print("4. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         print("View profile")
#     elif choice == 2:
#         print("Edit profile")
#     elif choice == 3:
#         print("Settings")
#     elif choice == 4:
#         print("Exit")
#         break
#     else:
#         print("Invalid choice")


# Q=5


# password=input("enter in password:")

# while len(password.strip())<8:
#     print("password in 8 chr.minium:")
#     password=input("enter in again password:")
# print("password is successfully")


# q=6

# temp=int(input("enter in tempature:"))
# while temp<-20 or temp>45:
#     temp=int(input("enter in correct tempature:"))
# print("tempature is correct!")


# Q=7

# balance=int(input("enter in amount:"))
# while balance<=0 or balance>5000:
#     balance=int(input("enter in correct balance:")) 
# print("correct amount")


# Q=8


# username = input("Enter username:")
# while len(username.strip()) < 5 or username.strip() == "" or " " in username.strip():      q=8
#     print("Invalid username")
#     username = input("Enter username:")
# print("Accepted username:", username.strip())


# Q=9

# n = int(input("Enter a positive integer: "))
# while n <= 0 or n % 3 != 0 or n % 5 != 0:
#     print("Invalid number!")
#     n = int(input("Enter a positive integer: "))
# print("Accepted number:", n)

    

# Q=10


# secret_pin = 2468
# for i in range(3):
#     pin = int(input("Enter your pin: "))
#     if pin == secret_pin:
#         print("Access granted")
#         break
# else:
#     print("Access denied")



# Q=11

# number = int(input("Enter a number: "))
# while number < 10 or number > 50:
#     print(" Enter a number between 10 and 50.")
#     number = int(input("Enter a number: "))    q=11
# print("Accepted value:", number)          
# if number % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")


# Q=12
# balance = 2000
# amount = float(input("Enter deposit amount:"))
# while amount <= 0:
#     print("Enter a positive amount")
#     amount = float(input("Enter deposit amount:"))
# balance = balance + amount
# print("New balance:", balance)


# Part B — Challenging Problems
# Q=13


# a=int(input("enter in numbers:"))
# while a<1 or a>100:
#     print("outside in range number:")
#     a=int(input("enter in numbers:"))
# print("correct numbers")
    

# Q=14

# a=int(input("enter in numbers:"))
# while a<1 or a>100:
#     print("number in again correct :")
#     a=int(input("enter in numbers:"))
# if a>75:
#     print("Distinction")
# elif 60<=a<=75:
#     print("First class")
# elif 35<=a<=60:
#     print("pass")
# else:
#     print("fail")

# Q=15


# user=input("enter in username:")
# password=input("enter in password:")
# while (len(user.strip())<5 or " " in user.strip() or (len(password.strip())<8 or password == " ")):
#     print("correct in user and password:")
#     user=input("enter in username:")
#     password=input("enter in password:")
# print("user and password correct")


# Q=16

# a=float(input("enter in numbers:"))
# operator=input("enter in (+,-,*,/):")
# while  operator not in ["+","-","*","/"]:
#     print("valid operator:")
#     operator=input("enter in (+,-,*,/):")
# b=float(input("enter in numbers:"))
# while b==0 or operator=="/":
#     print("valid in numbers:")
#     b=float(input("enter in numbers:"))
# if operator=="+":
#     print(a+b)
# elif operator=="-":
#     print(a-b)
# elif operator=="*":
#     print(a*b)
# else:
#     print(a/b)


# Q=17

# balance = 10000
# while True:
#     print("\n--- Banking Menu ---")
#     print("1. Check balance")
#     print("2. Deposit money")
#     print("3. Withdraw money")
#     print("4. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         print("Your balance is:", balance)
#     elif choice == 2:
#         amount = float(input("Enter deposit amount: "))
#         while amount <= 0:
#             print("Amount must be greater than zero!")
#             amount = float(input("Enter deposit amount again: "))
#         balance = balance + amount
#         print("Deposit successful!")
#         print("Updated balance:", balance)
#     elif choice == 3:
#         amount = float(input("Enter withdrawal amount: "))
#         while amount <= 0 or amount > balance:
#             print("Invalid amount! Check your balance.")
#             amount = float(input("Enter withdrawal amount again: "))
#         balance = balance - amount
#         print("Withdrawal successful!")
#         print("Updated balance:", balance)
#     elif choice == 4:
#         print("Thank you for using our bank!")
#         break
#     else:
#         print("Invalid choice! Please select 1 to 4.")


# Q=18

# month=int(input("enter in month:"))
# day=int(input("enter in days:"))
# while month<0 or month>12 or day<0 or day>31:
#     print("invalid month and day:")
#     month=int(input("enter in month:"))
#     day=int(input("enter in days:"))
# print("correct month and days:")


# Q=19


# quantity = int(input("Enter quantity: "))
# while quantity <= 0:
#     print("Invalid quantity!")
#     quantity = int(input("Enter quantity again: "))
# price = float(input("Enter unit price: "))
# while price <= 0:
#     print("Invalid price!")
#     price = float(input("Enter price again: "))
# total = quantity * price
# print("Total cost:", total)


# Q=20

# count=int(input("enter in count:-"))
# while count<1 or count>20:
#     print("invalid count:")
#     count=int(input("enter in count:-"))
# sum=0
# for i in range(1,count):
#     n=float(input("enter in numbers:"))
#     sum=sum+n
# avg=sum/count
# print("sum",avg)

# Q=21

# password=input("enter in password:-")
# while len(password)<8 or password=="A" or password=="a" :
#     print("invalid ")
#     password=int(input("enter in password:-"))
# print("valid password:") 

                                                                    #   q=21
# password = input("Enter password: ")
# while True:
#     if len(password) < 8:
#         print("Password must have at least 8 characters")
#     if not any(ch.isupper() for ch in password):
#         print("At least one uppercase letter required")
#     if not any(ch.islower() for ch in password):
#         print("At least one lowercase letter required")
#     if not any(ch.isdigit() for ch in password):
#         print("At least one digit required")
#     if any(ch.isspace() for ch in password):
#         print("Whitespace is not allowed")
#     if (len(password) >= 8
#         and any(ch.isupper() for ch in password)
#         and any(ch.islower() for ch in password)
#         and any(ch.isdigit() for ch in password)
#         and not any(ch.isspace() for ch in password)):
#         break
#     print("Invalid password! Try again.")
#     password = input("Enter password: ")
# print("Valid password!")





# Q=22


# n = int(input("Enter a number:"))
# while n < 1 or n > 10:
#     print("Invalid number")
#     n = int(input("Enter a number : "))
# print("Valid number:", n)



# Q=23


# s1=int(input("enter in score:"))
# while s1<0 or s1>100:
#     print("ivnalid score")
#     s1=int(input("enter in score:"))
# s2=int(input("enter in score:"))
# while s2<0 or s2>100:
#     print("ivnalid score")
#     s2=int(input("enter in score:"))
# s3=int(input("enter in score:"))
# while s3<0 or s3>100:
#     print("ivnalid score")
#     s3=int(input("enter in score:"))
# total=s1+s2+s3
# avg=total/3
# print("total",total)
# print("avarage",avg)



# Q=24

# balance=10000
# amount=int(input("enter in amount:"))
# while amount<=0 or amount>10000 or amount % 100 != 0:
#     print("invalid amount:")
#     amount=int(input("enter in amount:"))
# balance=balance-amount
# print("total amount:",amount)
# print("total balance",balance)




