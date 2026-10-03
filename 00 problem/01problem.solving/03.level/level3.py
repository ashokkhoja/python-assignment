# Q21. Count Digits in a Number
# count=0
# number=int(input("enter in numbers:-"))
# for i in range(len(str(number))):
#     count=count+1
# print(count,end="")

# Q22. Sum of Digits

# num=int(input("enter in numbres:-"))
# sum=0
# while num>0:
#     digit=num%10
#     sum=sum+digit
#     num=num//10
# print(sum,end="")


# Q23. Product of Digits


# num=int(input("enter in numbres:-"))
# sum=1
# while num>0:
#     digit=num%10
#     sum=sum*digit
#     num=num//10
# print(sum,end="")

# Q24. Reverse a Number
# sum=0
# num=int(input("enter in numbres:"))
# if num>0:
#     while num>0:
#         digit=num%10
#         sum=sum*10+digit
#         num=num//10
# else:
#     num=-num
#     while num>0:
#         digit=num%10
#         sum=sum*10+digit
#         num=num//10
#     print("-",end="")
# print(sum)


# Q25. Palindrome Number

# num = int(input("enter in number:-"))
# number = num
# reversed = 0
# while number > 0:
#     digit = number % 10
#     reversed = reversed * 10 + digit
#     number //= 10
# if num == reversed:
#     print("number is palindrome")
# else:
#     print("number is not palindrome")



# Q26. Prime Number (Simple Check)
# number = int(input("enter number: "))
# count = 0
# for i in range(1, number + 1):
#     if number % i == 0:
#         count += 1
# if count == 2:
#     print("true")
# else:
#     print("false")
    


# Q27. All Primes from 1 to N
# number = int(input("enter number: "))
# for i in range(2, number+1 ):
#     count = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i,end=" ")


# Q28. First N Fibonacci Numbers

# n = int(input("Enter N: "))
# a = 0
# b = 1
# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c

# # Q29. GCD of Two Numbers (Simple Loop)
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# gcd = 1
# for i in range(1, min(a, b) + 1):
#     if a % i == 0 and b % i == 0:
#         gcd = i
# print(gcd)
# # Q30. LCM of Two Numbers
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# for i in range(max(a, b), a * b + 1):
#     if i % a == 0 and i % b == 0:
#         print(i)
#         break
