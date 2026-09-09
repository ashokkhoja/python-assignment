#Level 1 — Intermediate
#1. Positive, Negative, or Zero
# num = float(input("Enter a number: "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

#2. Even or Odd + Positive or Negative
# num = int(input("Enter a number: "))
# if  num>0 and num % 2 == 0:
#     print("positive even")
# elif num>0 and num % 3 == 0:
#     print("positive odd")
# elif num<0 and num % -2 == 0:
#     print("negative even")
# elif num<0 and num % -3 == 0:
#     print("negative odd")
# else:
#     print("zero")

#3. Largest of Two Numbers

# num1=int(input("enter in first numbers:"))
# num2=int(input("enetr in second numbers:"))
# if num1>num2:
#     print("The larger number")
# elif num1>=num2:
#     print("Both are equal")
# else:
#     print("none")

#4. Smallest of Three Numbers
# a=int(input("enter in first numbers:"))
# b=int(input("enter in second numbers:"))
# c=int(input("enetr in third numbers:"))
# if a<b and a<c:
#     print("small number")
# elif a>c and c>b:
#     print("smallest number")
# else:
#     print("none")
  #5. Largest of Three Numbers
# x=int(input("enter in first numbers:"))
# y=int(input("enter in second numbers:"))
# z=int(input("enetr in third numbers:"))
# if x>y and x>z:
#      print("large number")
# elif y>z and x<z:
#      print("largeest number")
# else:
#      print("none")
#6. Divisible by 5 and 11

# m=int(input("enter in number:"))
# if m % 5==0 and m % 11==0 :
#     print("both 5 and 11")
# elif m %5==0:
#     print("only by 5")
# elif m % 11==0:
#     print("only by 11")
# else:
#     print("neither")

#7. Divisible by Either 3 or 7

# n=int(input("enter in number:"))
# if n%3==0 and n%7==0 :
#     print("3 and 7 both")
# elif n%3==0:
#     print("only 3")
# elif n%7==0:
#     print("only 7")
# else:
#     print("neither")

#8. Pass or Fail
# marks=int(input("enetr in marks:"))
# if marks<0 :
#     print("invalid marks")
# if marks>100:
#     print("Invalid marks")
# elif marks>=40 :
#     print("pass")
# elif marks<40:
#     print("fail")

#9. Grade Calculator

# m=int(input("enetr in first: "))
# if 90<m<100:
#     print("A")
# elif 80<m<89 :
#     print("B")
# elif 70<m<79:
#     print("C")
# elif 60<m<69:
#     print("D")
# elif 40<m<59:
#     print("E")
# else:
#     print("fail")

#10. Voting Eligibility
# age=int(input("enter your age :"))
# if age<0:
#      print("invalid age")
# elif age<18:
#   print("cannot vote")
# elif age>=120:
#    print("unrealistic age")
# else:
#     print("can vote")



#Level 2 — More Logical Conditions
#11. Leap Year
# year=int(input("enter in leap year:"))
# if year%400==0 or year%4==0 and year%100!=0:
#     print("leap year")
# else:
#     print("not a leap year")

#12. Character Type
# cha=input("character eord in :")
# if cha>='A' and cha<='Z':
#     print("Uppercase alphabet")
# elif cha>='a' and cha<='z':
#     print("Lowercase alphabet")
# elif cha>='0'and cha<='9':
#     print("Digit")
# else:
#     print("special character")
#13. Vowel or Consonant

char = input("Enter a character: ")

# Check if the input is a single character and an alphabet letter
# if len(char) == 1 and ((char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z')):
#     # Convert to lowercase logic using standard conditional checks
#     if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or \
#        char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
#         print("Vowel")
#     else:
#         print("Consonant")
# else:
#     print("Invalid input")
















#14. Profit or Loss
# cp=float(input("enter your cost price:"))
# sp=float(input("enter your selling price: "))
# if sp>cp:
#     print("profit",sp-cp)
# elif cp>sp:
#     print("loss",cp-sp)
# else:
#     print("No profit and no loss")


#15. Profit/Loss Percentage
# cost_price=float(input("enter in cost price"))
# selling_price=float(input("enter in selling price"))
# if selling_price>cost_price:
#     profit = selling_price - cost_price
#     print( "profit",profit / cost_price * 100)
# elif cost_price>selling_price:
#     loss = cost_price - selling_price
#     print("loss",loss / cost_price * 100)
# else:
#     print("none")

#16. Electricity Bill

  # bill=int(input("enter in electricity bill :"))
  # if 0=<bill<=100:
      
  #     print("₹5 per unit",bill*5)
  # elif 100<=bill<=200:
  #     print("₹7 per unit",bill*7)
  # else:
  #     print("₹10 per unit",bill*10)

#17. Simple Calculator
# first_number=int(input("enter your first number:"))
# second_number=int(input("enter your second number:"))
# operator=input("enter in operator(+,-,*,/)")
# if operator=="+":
#     print("jod",first_number+second_number)
# elif operator=="-":
#     print("baki",first_number-second_number)
# elif operator=="*":
#     print("guna",first_number*second_number)
# elif operator=="/":
#     print("bhag",first_number/second_number)
# else:
#     print("none")

#18. Temperature Classifier
# temp=int(input("enter your celsius:"))
# if temp<0:
#     print("freezing")
# elif 0<=temp<=15:
#     print("very cold")
# elif 16<=temp<=25:
#     print("cold")
# elif 26<=temp<=35:
#     print("normal")
# else:
#     print("Hot")

#19. Number Range Checker
# number=int(input("enter in number :"))
# if number<0:
#     print("Negative")
# elif 0<=number<=10:
#     print("between is 0 and 10")
# elif 11<=number<=50:
#     print("between is 11 and 50")
# elif 51<=number<=100:
#     print("between is 51 and 100")
# else:
#     print("above 100")
  #20. Triangle Validator  
# x= int(input("enter in first:"))
# y=int(input("enter in second:"))
# z=int(input("enter in third:"))
# if x+y>z and x+z>y and y+z>x:
#     print("valid triangle")
# else:
#     print("invalid triangle")
#Level 3 — Harder Conditional Problems
#21. Triangle Type
# m=int(input("enter your first side:"))
# n=int(input("enter your second side:"))
# b=int(input("enter your third side:"))
# if m+n>b and m+b>n and b+n>m:
#     print("Equilateral")
# elif m+n>b and m+b>n and b+n<m:
#     print("lsosceles")
# else:
#     print("Scalene")


#22. ATM Withdrawal
# account_balance=int(input("enter your account balance:"))
# withdrawal_amount=int(input("enter your withdrawal amount:"))
# if withdrawal_amount>0 and withdrawal_amount%100==0 and account_balance>withdrawal_amount and  withdrawal_amount+500<account_balance:
#      print("withdrawl successful")
#      print("remaining balance:", account_balance-withdrawal_amount)
# else:
#      print("none")

#23. Login System

# username=input("enter your username:")
# password=input("enter your password:")
# if username == "admin" and password== "python123":
#     print("login successful")
# elif username!="admin" and password=="python123" :
#     print("user not found")
# elif  username=="admin" and password!="python123" :
#     print("wrong password")
# else:
#     print("dono wrong h")

#
#24. Discount Calculator

# amount=int(input("enetr in purchase amount:"))
# if 0<amount<=499:
#     discounta=amount*0
#     print("Discount: 0%" "\nDiscount amount:",discounta, "\nFinal amount:",amount-discounta)
# elif 500<=amount<=999:
#     discounta=(amount*5)/100
#     print("Discount: 5%" "\nDiscount amount:",discounta, "\nFinal amount:",amount-discounta)
# elif 1000<=amount<=1999:
#     discounta=(amount*10)/100
#     print("Discount: 10%" "\nDiscount amount:",discounta ,"\nFinal amount:",amount-discounta)
# elif 2000<=amount<=4999:
#     discounta=(amount*15)/100
#     print("Discount: 15%" "\nDiscount amount:",discounta ,"\nFinal amount:",amount-discounta)
# elif amount>=5000:
#     discounta=(amount*20)/100
#     print("Discount: 20%" "\nDiscount amount:",discounta ,"\nFinal amount:",amount-discounta)    
# else:
#     print("please enter valid amount")


#25. Student Result System
# html=int(input("enter in html subjects marks:"))
# css=int(input("enter in css subjects marks: "))
# java=int(input("enter in java subjects marks:"))
# if 0<html<=100 and 0<css<=100 and 0<java<=100:
#     if html<35 or css<35 or java<35:
#         print("Fail")
#     else:
#         total=html+java+css
#         average=total/3
#         if average>=75:
#             print("Distinction")   
#         elif 60<=average<=74 :
#             print("First Class")
#         elif 50<=average<=59:
#             print("Second Class")
#         elif 35<=average<=49:
#             print("pass")
#         else:
#             print("not result found")
# 26 Date Validator
# day=int(input("enter in day:"))
# month=int(input("enter in month:"))
# year=int(input("enetr in year:"))
# if 0<day<32 and 0<month<13 and year>0:
#     if Month==1 or Month==3 or Month==5 or Month==7 or Month==8 or Month==10 or Month==12:
#         print("valid")
#     elif(Month==4 or Month==6 or Month==9 or Month==11) and Day<31:
#         print("valid")
#     elif (Month==4 or Month==6 or Month==9 or Month==11) and Day==31:  
#         print("date is not valid")  
#     else:
#         if Month==2 and (Year%400==0 or Year%4==0) and Year%100!=0 and Day==29:  
#             print("valid")  
#         elif Month==2 and Day<29:
#             print("valid")
#         else:
#             print("date is not valid")    
# else:
#     print("date is not valid")                     
    #27. Time Validator

# hours=int(input("enter in hours:"))
# minutes=int(input("enter in minutes:"))
# seconds=int(input("enter in seconds:"))
# if 0<hours<23:
#     if 0<minutes<59:
#         if 0<seconds<59:
#             print("valid time")
# else:
#             print("invalid time")


#28. Youngest of Three People
# persion1=input("enter in name:")
# age1=int(input("enter in age:"))
# persion2=input("enter in name:")
# age2=int(input("enter in age:"))
# persion3=input("enter in name:")
# age3=int(input("enter in age:"))
# if age1<age2 and age1<age3:
#     print(f"{persion1} is the youngest")
# elif age2<age1 and age2<age1:
#     print(f"{persion2} is the youngest")
# elif age3<age2 and age3<age2:
#     print(f"{persion3} is the youngest")
# else:
#     if age1==age2 and age2==age3 and age1!=age3:
#         print(f"{persion1} and {persion2} same")
#     elif age2==age3 and age2!=age3 and age2==age1:
#         print(f"{persion2} and {persion3} same")  
#     else:
#         print("three persion same")      
#29. Second Largest of Three Numbers
# num1=int(input("Enter number 1:"))
# num2=int(input("Enter number 2:"))
# num3=int(input("Enter number 3:"))
# if num1>num2 and num1>num3:
#     if num2>num3:
#         print(f"Middle number is {num2}")
#     else:
#         print(f"Middle number is {num3}")
# elif num2>num1 and num2>num3:
#     if num1>num3:
#         print(f"Middle number is {num1}")  
#     else:
#         print(f"Middle number is {num3}") 
# elif num3>num1 and num3>num2:
#     if num1>num2:
#         print(f"Middle number is {num1}")
#     else:
#         print(f"Middle number is {num2}")                     
# elif num1==num2==num3:
#     print(f"Middle number is {num2}")
# else:
#     if num1==num2:
#         print(f"Middle number is {num2}")
#     elif num1==num3:
#         print(f"Middle number is {num1}")
#     else:
#         print(f"Middle number is {num2}") 
#30. Complete Scholarship Decision ⭐
# student_age=int(input("Enter student age:"))
# marks=int(input("Enter student marks:"))
# family_income=int(input("Enter family income:"))
# attendance_percentage=int(input("Enter student attendance percentage:"))
# if 18<=student_age<=25 and 85<=marks<=100 and 0<=family_income<=30000 and  75<=attendance_percentage<=100:
#     print("Scholarship Approved")
# elif not 18<=student_age<=25:
#     print("Scholarship Rejected \nReason: Student age is not satisfied")
# elif not 85<=marks<=100:
#     print("Scholarship Rejected \nReason: Marks below 85")
# elif not 0<=family_income<=30000:
#     print("Scholarship Rejected \nReason: family income more than 30000") 
# elif not 75<=attendance_percentage<=100:
#     print("Scholarship Rejected \nReason: attendance is less than 75%")      
# else:
#     print("none")