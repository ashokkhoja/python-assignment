# Q=1

# def analyze_number(number):
#     if number<0:
#         negative=-number
#     else:
#         negative=number
#         even=number%2==0
#         digit=len(str(number))
#     return negative,even,digit
# print(analyze_number(789))
# print(analyze_number(744))


# Q=2

# def calculate_stats(a,b,c):
#     small=min(a,b,c)
#     big=max(a,b,c)
#     sum=a+b+c
#     return  small,big,sum
# print(calculate_stats(8,7,6))


# Q=3

# def make_sentence(subject,verb,object):
#     return subject+" "+verb+" "+object
# print(make_sentence(object="good.",verb="is",subject="Ashok"))


# Q=4

# def apply_discount(price, discount=0):
#     discount=price*discount/100
#     final_price=price-discount
#     return discount,final_price
# print(apply_discount(5000,10))

# Q=5

# def calculate_pay(hours,rate=200,bonus=0):
#     return hours * rate + bonus
# print(calculate_pay(5))
# print(calculate_pay(hours=5, rate=250, bonus=100))

# Q=6

# def get_coordinates(x=0, y=0):
#     return x,y
# print(get_coordinates(2))
# print(get_coordinates(y=8))
# print(get_coordinates(x=8,y=11))

# Q=7

# def compare(a, b):
#     if a>b:
#         return "A is grater",a-b
#     elif b>a:
#         return "B is grater",b-a
#     else:
#         return "Equal",0

# print(compare(8,5))

# Q=8


# def convert_temperature(value, scale="C"):
#     if scale == "C":
#         return (value * 9/5) + 32
#     elif scale == "F":
#         return (value - 32) * 5/9
# print(convert_temperature(25))
# print(convert_temperature(98.6, "F"))

# Q=9

# def calculate_result(marks, passing_marks=35):
#     if marks>=35:
#         return "pass"
#     else:
#         return "fail"

# print(calculate_result(78))

# Q=10

# def order_summary(item, quantity=1, price=100, delivery_fee=40):
#     total=quantity*price*delivery_fee
#     return total 
# print(order_summary("gold"))
# print(order_summary(delivery_fee=80,price=0.1))
