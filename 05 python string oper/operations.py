#Task=1
a="ashok"
b='nagaur'
c="html"
d="khatu baba ki jay"
print(a,b,c,d)
#Task=2
a=""
print(a)
print(len(a))
print(type(a))
#Task=3
h="Python Programming"
print(h)
print(len(h))
print(h[0])
print(h[-1])
print(h[2])
print(h[-2])
#Task=4
x="Programming"
print(x[0])
print(x[1])
print(x[5])
print(x[-1])
#Task=5
a="Programming"
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-11])
#Task=6
h="ashokkhoja"
print(h[0])
print(h[-1])
print(h[-1])
#Task=7
m="python programming"
print(m[0:6])
print(m[7:18])
print(m[0:18])
print(m[0:5])
print(m[-5:])
#Task=8
a="ABCDEFGHIJKL"
print(a[::2])
print(a[::3])
print(a[1:8:2])
print(a[::-1])
#Task=9
x="python programming"
print(x[-5:])
print(x[-10:])
print(x[::-1])
#Task=10
c="python programming"
print(c[0:3])
print(c[-3:])
print(c[0::2])
print(c[::-1])
print(c[1:-1])
#Task=11
a="ashok"
b="ashokkhojabhojas"
c="bhojas tantwas"
print(len(a))
print(len(b))
print(len(c))
#Task=12
text = "Python Programming"

last_index = len(text) - 1
print( last_index)
print( text[last_index])
#Task=13
first_name="ashok"
last_name="khoja"
print(first_name+"  "+last_name)
#Task=14
name="ashok"
age="16"
city="nagaur"
language="css"
print(name+" "+age+" "+city+" "+language)
#Task=15
name="ashok"
age=17
print("my name is" + name)
print("my age is" + str(age))
#Task=16
a="tejal"
print(a*3)
print(a*5)
print(a*8)
#Task=17
a="*"
print(a*10)
#Task=18
b="python programming language"
print(b.upper())
print(b.lower())
print(b.capitalize())
print(b.title())
print(b.swapcase())
#Task=19
X = "Python"
Y = "python"
print(X == Y)
X = X.lower()
Y = Y.lower()
print(X == Y)

#Part 10 — Searching
#Task 20 — Membership
X = "Python is a programming language"
print("Python" in X)
print("programming" in X)
print("java" in X)
print("language" in X)

#Task 21 — find()
X = "Python is a programming language"
print(X.find("python"))
print(X.find("programming"))
print(X.find("language"))
print(X.find("Java"))

#Task 22 — index()
X = "i love you my dear brother"
result = X.index("my")
print(result)

#Task 23 — Count Characters
A = "banana"
print(A.count("a"))
print(A.count("n"))
print(A.count("b"))

#Task 24 — Starts and Ends
filename = "student_notes.pdf"
a=filename.startswith("student")
b=filename.endswith(".pdf")
c=filename.endswith(".txt")
print(a)
print(b)
print(c)

#Task 25 — Replace a Word
text = "I am learning Java"
a=text.replace("Java","python")
print(a)

#Task 26 — Multiple Replacements
text = "apple apple apple"
a=text.replace("apple","mango",3)
print(a)

#Task 27 — Limited Replacement
text = "apple apple apple"
a=text.replace("apple","mango",1)
print(a)

#Task 28 — Check Immutability
text = "Python"
b=text.upper()
print(b)
print(text)

#Part 12 — Whitespace
#Task 29
text = "   Python Programming   "
a=text.strip()
print(a)
b=text.lstrip()
print(b)
c=text.rstrip()
print(c)

#Task 30 — User Input


#Part 13 — Split and Join
#Task 31 — Split
a="Python is easy to learn"
print(a.split())

#Task 32 — Split with Separator
b="apple,banana,mango,orange"
print(b.split(","))

#Task 33 — Join
words = ["Python", "is", "easy"]
print(" ".join(words))

#Task 34 — Join with Different Separators
words = ["Python", "is", "easy"]
print("-".join(words))
print("/".join(words))

#Part 14 — String Formatting
#Task 35 — F-String
name="ashok"
age="17"
city="nagaur"
print(f"my name is {name} i old in {age} i live in {city}.")

#Task 36 — Arithmetic Inside F-String
a = 10
b = 20
c=10+20
print(f"The sum is {c}")

#Part 15 — Error Identification
#Task 37
text = "Python"
print(text[0:])
#indexerror in print in task 37

text = "Python"

#print(sytanx error in task37)
print("j"+text[1:])

age = 20
print("Age: " +str ("age"))
#print(TypeError in)

text = "Python"
print(text.index("Python"))
#print(valueerror)

#Part 16 — Practical Challenge
#Task 38 — Name Processor

name= input("Enter your full name:")
user=name.strip()
print(name)
print(user)
print(name.upper())
print(name.lower())
print(name.title())
print(len(name))
print(name[0])
print(name[-1])
print("a" in name)

#Part 17 — Practical Challenge
#Task 39 — Sentence Analyzer
user_sentence=input("Enter your sentence:")

print("The original sentence is :",user_sentence.strip())
length=len(user_sentence)
print("Number of characters is :",length)
list=user_sentence.split()
words=len(list)
print(words)
print(user_sentence[-length])
print(user_sentence[length-1])
print(user_sentence.upper())
print(user_sentence.lower())
print(user_sentence.title())
print("Python" in user_sentence)
chiose_char=input("Enter your character to find in sentence:")
print(user_sentence.count(chiose_char))

#Part 18 — Final Challenge
#Task 40 — Student Information

your_fname=input("Enter your First name:")
your_lname=input("Enter your Last name:")
your_city=input("Enter your City:")
your_course=input("Enter your Course:")
your_age=(input("Enter your age:"))

#1
print(your_fname.strip())
print(your_lname.strip())
print(your_city.strip())
print(your_course.strip())
print(your_age.strip())

#2
fullname=your_fname+" "+your_lname
print(fullname)

#3
print(fullname.title())

#4
print(fullname.upper())

#5
print(fullname.lower())

#6
length=len(fullname)
print(length)

#7
print(fullname[-length])

#8
print(fullname[length-1])

#9
print(your_city,"and",your_course)

#10
print(f"my age is {your_age}")

#11
print("Python" in your_course  or "Python" in your_course.title())

#12
tyour_course=your_course.title()
print(tyour_course.replace("Python","Java"))

#13
list=your_course.split()
words=len(list)
print(words)








