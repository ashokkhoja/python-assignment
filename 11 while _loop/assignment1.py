A. Basic for Loop
1.
i=1
while i<6:
    print("Hello")
    i+=1

2.
i=0
while i<10:
    print(i,end="")
    i+=1

3

i=1
while i<11:
    print(i,end="") 
    i+=1

4
i=10
while i>0:
    print(i,end="")
    i-=1

5
i=5
while i<51:
    print(i)
    i+=5

6
i=2
while i<21:
    print(i)
    i+=2

7
i=1
while i<20:
    print(i)
    i+=2


8

i=3
while i<19:
    print(i)
    i+=3

9
i=20
while i>1:
    print(i)
    i-=2

10
n=int(input("enter in numbers:-"))
i=1
while i<=n:
    print(i)
    i+=1

11
n=int(input("enter in numbers:-"))
i=2
while i<=n:
    print(i)
    i+=2

12
n=int(input("enter in odd numbers:-"))
i=1
while i<=n:
    print(i)
    i+=2

13
n=int(input("enter in numbers:-"))
i=3
while i<=n:
    print(i)
    i+=3

14
n=int(input("enter in numbers:-"))
i=1
while i<=n:
 if i%2==0 and i%3==0:
     print(i)
 i+=1    

15

n=int(input("enter in numbers:-"))
i=2
count=0
while i<=n:
    print(i,end=" ")
    i+=2
    count+=1
    print("count",count)

16
n=int(input("enter in numbers:-"))
i=1
total=0
while i<=n:
    print(i,end=" ")
    i+=1
    total=total+i
print("total",total)

17
n=int(input("enter in numbers:-"))
i=2
total=0
while i<=n:
    print(i)
    i+=2
    total=total+i
print("sum total",total)

18
n=int(input("enter in numbers:-"))
i=1
total=0
while i<=n:
    print(i)
    i+=2
    total=total+i
print("odd total",total)

19
n=int(input("enter in numbers:-"))
i=1
while i<=10:
    print(i*n)
    i+=1

20
n=int(input("enter in numbers:-"))
i=1
total=1
while i<=n:
    print(i)
    total=total*i
    i+=1
print("total:-",total)
   
21
string=input("enter in name :-")
i=0
while i<len(string):
    print(string[i])
    i+=1

22
string=input("enter in name :-")
i=0
while i<len(string):
    print(string[i],end="")
    i+=1

23
string=input("enter in name :-")
i=0
count=0
while i<len(string):
    print(string[i], end="")
    i+=1
    count+=1
print("count", count)

24
n = input("Enter a string: ")
count = 0
i = 0
while i< len(n):
    if n[i] == 'a':
        print(n[i])
        count += 1
    i+= 1
print("count",count)

25
n=input("enter in name:-")
count=0
i=0
while i<len(n):
    if chr(65)<=n[i]<=chr(90):
        print(n[i])
        count+=1
    i+=1
print("uppercase count",count)  

26  
i=1
while i < 4:
    j = 1
    while j < 5:
        print("*", end="")
        j += 1
    print()
    i += 1 

27
i=1
while i<5:
    j=1
    while j<6:
        print("*",end="")
        j+=1
    print()
    i+=1

28
i=1
while i<=5:
    j=1
    while j<=i:
        print("*",end="")
        j+=1
    print()
    i+=1

i=1
while i <= 5:
    print("*" * i)
    i += 1
29
i=1
while i<=5:
     j=1
     while j<=i:
         print(j,end="")
         j+=1
     print()
     i+=1
30
n=int(input("enter in numbers:-"))
i=1
while i<=n:
    j=1
    while j<=10:
     print(f"{i}*{j}={i*j}")
     j+=1
    print()
    i+=1