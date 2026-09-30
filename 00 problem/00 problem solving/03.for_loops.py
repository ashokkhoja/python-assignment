# 1. Digit and chrracter Analyzer
# uppercasecount=0
# lowercount=0
# spacescount=0
# specialcount=0
# digitscount=0
# string=input("enter in chrracters:")
# for i in string:
#     if chr(65)<=i<=chr(90):
#         print("uppercase:")
#         uppercasecount+=1
#     elif chr(97)<=i<=chr(122):
#         print("lowercase:")
#         lowercount+=1
#     elif chr(48)<=i<=chr(57): 
#         print("digits:")
#         digitscount+=1
#     elif chr(32)==i:
#         print("space")
#         spacescount+=1
#     else:
#         print("special")
#         specialcount+=1
# if uppercasecount>lowercount and uppercasecount>digitscount and uppercasecount>spacescount and uppercasecount>specialcount:
#     print("uppercase highest")
# elif lowercount>uppercasecount and lowercount>digitscount and lowercount>specialcount and lowercount>spacescount:
#     print("loewrcase highest")
# elif spacescount>uppercasecount and spacescount>digitscount and spacescount>specialcount and spacescount>lowercount:
#     print("spacescount highest")
# elif specialcount>uppercasecount and specialcount>lowercount and specialcount>digitscount and specialcount>spacescount:
#     print("specialcount highest")
# elif digitscount>uppercasecount and digitscount>lowercount and digitscount>spacescount and digitscount>specialcount:
#     print("digitscount highest")
# else:
#     print("Tie")


# print(uppercasecount)
# print(lowercount)
# print(digitscount)
# print(spacescount)
# print(specialcount)

# 2. Student Performance Analyzer
# excellentcount=0
# goodcount=0
# passcount=0
# failcount=0
# for i in range(1,11):
#     marks=int(input("enter in marks:"))
#     if 75<=marks<=100:
#         print(("excellent"))
#         excellentcount+=1
#     elif 50<=marks<=74:
#         print("Good")
#         goodcount+=1
#     elif 35<=marks<=49:
#         print("Pass")
#         passcount+=1
#     else:
#         print("fail")
#         failcount+=1

#     print(excellentcount)
#     print(goodcount)
#     print(passcount)
#     print(failcount)


# 3. chr Score Calculator
# vowelcount = 0
# consonantcount = 0
# digitcount = 0
# specialcount = 0

# sentence = input("Enter in string:-")
# word = sentence.split()
# print(word)
# highestscore = 0
# highestword = ""
# for i in word:
#     score = 0
#     for j in i:
#         if j in "aeiouAEIOU":
#             print("vowel")
#             vowelcount += 2
#             score += 2
#         elif j in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
#             print("consonant")
#             consonantcount += 1
#             score += 1
#         elif chr(48) <= j <= chr(57):
#             print("digits")
#             digitcount += 3
#             score += 3
#         else:
#             print("special")
#             specialcount += 4
#             score += 4
#     print(i, "score =", score)
#     if score > highestscore:
#         highestscore = score
#         highestword = i
# print("Highestword:", highestword)
# print("Highestscore:", highestscore)

# print("Consonantpoints:", consonantcount)
# print("Vowelpoints:", vowelcount)
# print("Digitpoints:", digitcount)
# print("Specialpoints:", specialcount)

# 4. Password Batch Validator
# lenth=0
# uppercount=0
# lowercount=0
# digitcount=0
# specialcount=0
# password=input("enter in password:-")
# for i in password:
#     lenth+=1
#     if chr(65)<=i<=chr(90):
#         uppercount+=1
#     elif chr(97)<=i<=chr(122):
#         lowercount+=1
#     elif chr(48)<=i<=chr(57):
#         digitcount+=1
#     else:
#         specialcount+=1
# if lenth>=8 and uppercount>=1 and lowercount>=1 and digitcount>=1 and specialcount>=1:
#     print("Strong")
# elif lenth>=8 and (uppercount>=1 or lowercount>=1) and digitcount>=1:
#     print("Medium")
# else:
#     print("Weak")
# print("Length:",lenth)
# print("Uppercase:",uppercount)
# print("Lowercase:",lowercount)
# print("Digits:",digitcount)
# print("Special:",specialcount)
        
# 5. Sentence Word Analyzer
# sentence=input("enter in sentence:-")
# short=0
# medium=0
# long=0
# for i in sentence.split():
#     lenth=0
#     for j in i:
#      lenth+=1
#     print(i,lenth)
#     if lenth<=3:
#         print("Short")
#         short+=1
#     elif lenth<=6:
#         print("Medium")
#         medium+=1
#     else:
#         print("Long")
#         long+=1
# print("Short",short)
# print("Medium",medium)
# print("Long",long)
    
# 6. Number-String Conversion Challenge
# evencount=0
# oddcount=0
# for i in range(5):
#     num=int(input("enter in numbers:-"))
#     num=str(num)
# for j in num:
#     if int(j)%2==0:
#         print("even")
#         evencount+=1
#     else:
#         print("odd")
#         oddcount+=1
# if evencount>oddcount:
#     print("even  ",evencount)
# elif evencount<oddcount:
#     print("odd ",oddcount)
# else:
#     print("equal")

# 7. Repeated Character Report
# duplicate = 0
# repeat = 0
# highrepeat = 0
# string = input("enter in string characters:")
# for i in string:
#     count = 0
#     for j in string:
#         if i == j:
#             count += 1
#     if count == 2:
#         print(i, "duplicate")
#         duplicate += 1
#     elif count == 3 or count == 4:
#         print(i, "repeat")
#         repeat += 1
#     elif count >= 5:
#         print(i, "highly repeat")
#         highrepeat += 1
# print("duplicate word:", duplicate)
# print("repeat word:", repeat)
# print("highly repeat word:", highrepeat)

# 8. Shopping Cart Analyzer
# total = 0
# budget = 0
# regular = 0
# premium = 0
# luxury = 0
# for i in range(8):
#     price = int(input("Enter product price:"))
#     total += price
#     if price < 500:
#         print("Budget")
#         budget += 1
#     elif 500 <= price <= 1999:
#         print("Regular")
#         regular += 1
#     elif 2000 <= price <= 4999:
#         print("Premium")
#         premium += 1
#     else:
#         print("Luxury")
#         luxury += 1
# average = total / 8
# print("Totalamount:", total)
# print("Budget:", budget)
# print("Regular:", regular)
# print("Premium:", premium)
# print("Luxury:", luxury)
# print("Average:", average)

# 9. Character Position Challenge
# vowel=0o
# consonant=0
# digit=0
# special=0
# string=input("enter in character:-")
# print(string)
# position=0
# for i in string:
#     if positin%2==0:
#         print("even position")
#     else:
#         print("odd position")
#     if i in "aeiouAEIOU":
#         print("vowel")
#         vowel+=1
#     elif i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
#         print("consonant")
#         consonant+=1
#     elif chr(48)<=i<=chr(57):
#         print("digit")
#         digit+=1
#     else:
#         print("special")
#         special+=1
#     position+=1
#     print()
# print("vowel",vowel)
# print("consonant",consonant)
# print("digit",digit)
# print("special",special)

# 10. Number Pattern With Condition

# n=int(input("enter in numbers:-"))
# for i in range(n):
#    for j in range(1,i*2+2):
#       if j%3==0:
#          print("x",end="")
#       elif j%5==0:
#          print("Y",end="")
#       elif j%3==0 and j%5==0:
#           print("z",end="")
#       else:
#         print(j,end="")
#    print()
      
# 11. Username Analyzer
# digitscount=0
# underscorecount=0
# for i in range(5):
#     usernames=input("enter in usernames:-")
#     for j in usernames:
#      lenth=0
#      if j=="1":
#         print("valid",end="")
#         lenth+=1
#      elif chr(48)<=j<=chr(57):
#         print("needs improvement",end="")
#         digitscount+=1
#      elif j=="_":
#         print("invalid",end="")
#         underscorecount+=1
#      else:
#         print(j,end="")
#     print(lenth)
#     print(digitscount)
#     print(underscorecount)








     
        
     

    



