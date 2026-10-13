# Section A --- Practice Problems on break

# Q=1

# for i in range(1, 8):
#     if i == 5:
#         break
#     print(i)
# print("Finished")   

# output:-1,2,3,4 finished


# Q=2

# word = "skyline"
# for ch in word:
#     if ch in "aeiou":
#         break
#     print(ch)


# output:-skyl


# Q=3

# n = 2
# while n <= 10:
#     print(n)
#     if n == 6:
#         break
#     n += 2


# output:-2,4,6



# Q=4


# n=int(input("enter in numbers:-"))

# for i in range(1,n):
#     if i==7:
#         break
#     print(i)


# Q=5

# n=input("enter in string:-")
# for i in n:
#     print(i)
#     if i=="p":
#         break

# Q=6

# n=[1,5,8,-5,5]
# for i in n:
#     if i<0:
#         break
#     print(i)

# Q=7

# for row in range(1, 4):
#     for col in range(1, 5):
#         if col == 3:
#             break
#         print(row, col)


# output:-1 1
#         1 2
#         2 1
#         2 2
#         3 1
#         3 2
    

# Q=8

# a="python makes coding fun"
# a="python"
# flag=False
# for i in a.split():
#     if i==a:
#         print("found")
#         flag=True
#         break
# if not flag:
#     print("not found")




# Section B ---

# Q=9\

# for i in range(1, 7):
#     if i == 4:
#         continue
#     print(i)


# output:-1,2,3,5,6



# Q=10

# for ch in "education":
#     if ch in "aeiou":
#         continue
#     print(ch, end="")


    # output:-dctn


# Q=11

n = 0

# while n < 5:
#     n += 1
#     if n == 3:
#         continue
#     print(n)

    # output:-1,2,4,5


# Q=12

# n=int(input("enter in numbers:-"))
# for i in range(1,n):
#     if i%3==0:
#         continue
#     print(i)


# Q=13

# str=input("enter in string:-")
# for i in str:
#     # a=input("enter in word:")
#     if i=="s":
#         continue
#     print(i)


# Q=14

# marks=[24, 10, 20, 29, 30]
# flag=False
# for i in marks:
#     if i<40:
#         continue
#     print(i)
#     flag=True
# if not flag:
#     print("no marks printed")


# Q=15

# for i in range(1, 5):
#     if i == 2:
#         continue
#     print("A", i)
#     print("B", i)


    # output:-A,1
    #         B,1
            # A 3
#             B 3
#             A 4
#             B 4


# Q=16


# n = 0

# while n < 5:
#     n+=1
#     if n == 3:
#         continue
#     print(n)
# n += 1
   

# Q=17

# n=input("enter in word:-")
# count=0
# for i in n:
#     if i=="a" or i=="e" or i=="i" or i=="o"  or i=="u":
#         continue
#     count+=1
#     print(count)


# Section C---


# Q=18


# for i in range(1, 4):
#     print(i)
# else:
#     print("Done")


#     output:-1,2,3 done


# Q=19

# for i in range(1, 5):
#     if i == 2:
#         continue
#     print(i)
# else:
#     print("Completed")

# output:-1,3,4 complete


# Q=20

# for i in range(1, 5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Completed")
# print("Outside loop")


# output:-1,2 outside loop


# Q=21

# for item in []:
#     print("Inside")
# else:
#     print("Else block")


#     output:-Else block


# Q=22


# n = [1, 5, 4, 8, 9, 6, 3, 4]
# a = 0
# for i in n:
#     if i == a:
#         print("Found")
#         break
# else:
#     print("Not found")


# Q=23

# n=input("enter in string:-")
# a="g"
# for i in n:
#     if i==a:
#         print("Character exists")
#         break
# else:
#     print("Character missing")

# Q=24

# n = int(input("Enter a number: "))
# for i in range(2, n):
#     if n % i == 0:
#         print("Not prime")
#         break
# else:
#     print("Prime")

# Q=25

# values = [2, 4, 6, 8]
# for value in values:
#     if value % 2 != 0:
#         print("Odd found")
#         break
# else:
#     print("All are even")

#     output:-all are even


# Q=26
# C-A
# for x in range(3):
#     continue
# else:
#     print("A")

# output:-A

# C-B
# for x in range(3):
#     break
# else:
#     print("B")


#     output:-empty 

# C-C

# for x in range(0):
#     print(x)
# else:
#     print("C")

# output:-C


# Q=27

# str=input("enter in string:-")                                  q=27
# for i in range(len(str)):
#     if str[i] in str[i+1:]:
#         print(str[i])
#         break
# else:
#     print("no repeates character")


# Section D --- 

# Q=28

# for i in range(1, 4):
#     if i == 2:
#         pass
#     print(i)

#     output:-1,2,3

# Q=29

# x = 10
# if x > 5:
#     pass
# print("Finished")


# output:-finished

# Q=30

# for letter in "cat":
#     pass

# print("Loop ended")

# output:-loop ended


# Q=31
# n=int(input("enter in numbers:"))
# for i in range(1,n):
#     if i%2==0:
#         pass
#     print(i)


# Q=32

# for i in range(1,10):
#     if i==1:
#         pass
#         print("1 The message for option 1, then `Program closed")
#     elif i==2:
#         pass
#         print("2 No action for option 2, then `Program closed")
# else:
#     print("9 The message for an unknown option, then `Program closed")



# or 


# n = int(input("Enter your numbers: "))
# if n == 1:
#     print("The message for option 1")
# elif n == 2:
#     pass
# else:
#     print("The message for an unknown option")

# print("Program closed")



# Q=33
# A

# for i in range(1, 5):
#     if i == 3:
#         pass
#     print(i)

# output:-1,2,3,4

# B

# for i in range(1, 5):
#     if i == 3:
#         continue
#     print(i)

# output:-1,2,4


# Q=34

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)



# Section E ---


# Q=35

# for i in range(1, 6):
#     if i == 2:
#         continue
#     if i == 4:
#         break
#     print(i)
# else:
#     print("Finished")

# output:-1,3


# Q=36

# a=[5,4,8,-2,-6,5]
# for i in a:
#     if i<0:
#         continue
#     if i==8:
#         print("Target found")
#         break
# else:
#     print("target not found")


# Q=37

# a= [12,  5,  18, 20]
# for i in a:
#     if i == 0:
#         continue
#     if i == -1:
#         break
#     print(i)
# else:
#     print("All values processed")

# Q=38

# for row in range(1, 4):
#     for col in range(1, 4):
#         if col == 2:
#             continue
#         if row == 3:
#             break
#         print(row, col)
#     else:
#         print("Inner loop completed")


        # output:=1 1
#                 1 3
#               Inner loop completed
#                 2 1
#                 2 3
#               Inner loop completed



# Q=39

# a=list (map(int,input("enter in numbers:-").split()))
# for i in a:
#     if i<0:
#         continue
#     if i%4==0 and i%6==0:
#         print("found:",i)
#         break
# else:
#     print("no matching number")


# Q=40

# 1=>break
# 2=>continue
# 3=>for-else
# 4=>pass
# 5=>continue
# 6=>break
# 7=>for-else
# 8=>pass

        
    

