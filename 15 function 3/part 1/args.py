# Q=1

# def multiply_all(*args):
#     result = 1
#     for num in args:
#         result = result * num
#     return result
# print(multiply_all(2, 3, 4))
# print(multiply_all(5, 6))
# print(multiply_all())


# Q=2
 
# def print_profile(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)

# print_profile(name="Ravi", age=21, city="Ahmedabad")


# Q=3

# def make_message(name, /, *, greeting="Hello"):
#     print(greeting, name)

# make_message("Ravi")
# make_message("Ravi", greeting="Good Morning") 


# Q=4

# def add(a, b, c):
#     print(a + b + c)

# values = [4, 5, 6]

# add(*values)


# Q=5

# def person_info(name, age):
#     print(name)
#     print(age)

# person = {"name": "Ravi", "age": 21}

# person_info(**person)


# Q=6

# def square(number):
#     return number * number

# print(square(5))


# Q=7

# def rectangle_area(length: float, width: float) -> float:
#     return length * width

# print(rectangle_area(10, 5))


# Q=8

# def add(a: int, b: int) -> int:
#     return a + b

# print(add("Hello", "World"))


# Q=9

# def student(name):
#     print(name)

# student("Ravi", **{"name": "Amit"})


# Q=10

# def show(*args):
#     print(args)

# show(10, 20, 30)