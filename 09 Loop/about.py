#Q=1
# for i in range(5):
#     print("Hello")
#Q=2
# for i in range(0,10):
#     print(i,end=" ")
#Q=3
# for number in range(1,11):
#     print(number)
#Q=4
# for i in range(10,0,-1):
#      print(i)
#Q=5
# for numbers in range(5,55,5):
#     print(numbers)

#Q=6
# for i in range(2,21,2):
# if i%2==0:
#         print("even",i)
#Q=7
# for i in range(1,20):
#     if i%2!=0:
#         print(i)
#Q=8
# for i in range(3,19,3):
#     print(i)
#Q=9
# for i in range(20,2,-2):
#     print(i)
#Q=10
# n = int(input("Enter a positive integer: "))

# for i in range(1, n + 1):
#     print(i)


#C. Conditions with for
#Q=11
# n=int(input("enter in even numbers:"))

# for i in range(1,n+1):
#     if i%2==0:
#         print(i)

#Q=12

# n=int(input("enter in odd numbers:"))

# for i in range(1,n+1):
#      if i%2!=0:
#          print(i)

#Q=13
# n=int(input("enter in 3 divided numbers:"))
# for i in range(1,n+1):
#     if i%3==0:
#         print(i)

#Q=14
# n=int(input("enter in 2 and 3 numbers:"))
# for i in range(1,n+1):
#     if i%2==0 and i%3==0:
#         print(i)

#Q=15
# n = int(input("Enter a positive integer: "))
# count = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#        count=count+1

# print(count)


#D. Calculation Problems
#Q=16

# n=int(input("enetr in n numbers:"))
# total=0
# for i in range(1,n+1):
#     total = total + i
#     print(total)

#Q=17
# n=int(input("enter in numbers:"))
# sum=0
# for i in range(1,n+1):
#     if i%2==0:
#         sum=sum+1
#         print(sum)

# #Q=18
# n=int(input("enter in numbers:"))
# sum=0
# for i in range(1,n+1):
#     if i%2!=0:
#         sum=sum+i
# print(sum)


#Q=19
# number=int(input("enter in numbers :"))
# for i in range(1,11):
#     mul=number*i
#     print(mul)

#Q=20
# n=int(input("enter in calculate:"))
# mul=1
# for i in range(1,n+1):
#     mul=mul*i
#     print(mul)


#E. String Iteration
Q=21
# name=input("enter your name:")
# for i in name:
#     print(i)

# #Q=22
# name=input("enter your name:")
# for i in name:
#     print(i,end=" ")

#Q=23
# name=input("enter your name:")
# count=0
# for i in name:
#     count=count+1
# print(count)

#24
# name=input("enter your name:")
# count=0
# for i in name:
#     if i=="a":
#         count=count+1
# print(count)

#Q=25
# name=input("enter your name:")
# count=0
# for i in name:
#     if ord(i)<=91 and ord(i)>=65:
#         count=count+1
# print(count)

#Q=26
# for row in range(3):
#     for col in range(4):
#          print("*",end="")
#     print()

#Q=27
# for row in range(4):
#     for col in range(5):
#          print("*",end="")
#     print()
   
#Q=28

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# Q=29
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


#Q=30

# for i in range(5):
#     for j in range(5):
#         print((i+1)*(j+1),end="\t")
#     print()



#final challenge pratice

n=int(input("enter in numbers:"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end="")
    print()    

