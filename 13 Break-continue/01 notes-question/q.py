#Q=1
i=1
while True:
    num=int(input("enter in numbers:-"))
    if num==0:
        break
    if num<0:
        continue
    print(num)


#Q=2

numbers = [12, 5, -4, 18, 0, 25, 30]
for i in numbers:
    if i==0:
        break
    if i<0:
        continue
    print(i)


#Q=3
numbers = [12, 5, -4, 18, 0, 25, 30]
for i in numbers:
    if i==0:
        print("Number found")
        break
    else:
        print("Number not Found")
    

        