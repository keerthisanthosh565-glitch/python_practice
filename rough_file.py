# # txt = "hello, and welocome to my world"
# # x = txt .capitalize()  # Hello,and welcome (1st letter capital)
# # print(x)               (1)

# # txt = "Hello, and welocome to my world"
# # x = txt .lower() # small        (2)
# # print(x)
 
# print("Hello World")
# print("Have a good day")            (3)
# print("Learning Python is fun") # thazhe thazhe varan

# print("Hello World");print("Have a good day");print("Learning Python is fun")

# print("I am", 35, "years old.") # mix of txt and numb
# x = 4       # x is of type int
# x = "Sally" # x is now of type str
# print(x)    


# x = "Python"
# y = "is"                (4)
# z = "awesome"
# print(x, y, z) # python is aswesome (nere vann)

# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z) # vere step same kariythin

# b = "Hello, World!"
# print(b[2:5]) # last numb kanan    (5)

# b = "Hello, World!"
# print(b[2:]) # 1st digt kazinj olla baaki numb

# x = 5
# print(x > 0 and x < 10) # and function    (6)

# x = 5
# print(x < 5 or x > 10) # or function

# x = 5
# print(not(x > 3 and x < 10)) # not function
#*********************************************
#*********************************************

# a = 33
# b = 200                            (7)
# if b > a:
#   print("b is greater than a") #if

#************************************************************
# a = 33
# b = 33
# if b > a:                                 (8)
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal") #- if 
#******************************************************************
# number = 5

# if number > 10:
#     print("Big") # 10 nne kaal big no 5 nn(no) nxt condition

# elif number == 5:
#     print("Correct") # same                        (9)

# else:
#     print("Small")  # satisfy aayilel else kodth
#************************************************************8
# number = 7    # if and else

# if number % 2 == 0:
#   print("The number is even")                      (10)
# else:
#   print("The number is odd")
#**************************************************************************
# i = 1
# while i < 6:
#   print(i)                                                   (11)                                          
#   i += 1

#******************************************************************************
# variables
name= "keerthi"
age = 24
place = "kottayam"

print(name)
print(age)
print(place)

#2
num1 = 10
num2 = 20
print(num1 + num2)

#3
num1= 10
num2 = 10.5
print(type(10))
print(type(10.5))
print(type("python"))
print(type(True))

#4
# name = input("enter your name")
# print("welcome",name)

#5
a = 10
b = 20
a,b = b,a
print("a=",a)
print("b=",b)

#operators
#6
num1 = 10
num2 = 20
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

#7
remainder = 24 % 4
print("Remainder:",remainder)

#8
num1 = 10
num2 = 20
print("are equal",num1 == num2)

#9
length = 3
width = 4
area = length * width
print(length * width)

#10
num1 = 10
num2 = 20
num3 = 30
average = (num1 + num2 + num3)/3
print("Average:",average)

#if,elif,else
#11
# num = float(input("enter a number"))
# if num > 0:
    # print("positive")
# elif num < 0:
    # print("negative")

# else:
    # print("zero")

#12
# num = int(input("enter a number:"))
# if num % 2 == 0:
#     print("even number")
# else:
#     print("odd number")

#13
# num =int(input("enter a age:"))
# if age >=18:
#     print("eligible")
# else:
#     print("not eligible")

#14
# a= float(input("enter first number:"))
# b = float(input("enter second number:"))
# c = float(input("enter third number:"))

# if a >= b and a >= c:
#     print("larger number:",a)
# elif b >=a and b >=c:
#     print("larger number:",b)
# else:
#     print("larger number:",c)

#15
# marks = int(input("enter your mark:"))
# if marks >= 90:
#     print("grade A")
# elif marks >=80:
#     print("grade B")
# elif marks >= 70:
#     print("grade C")
# else:
#     print("fail")

#loop
#16
for i in range(1,11):
    print(i)
#17
for i in range(2,51,2):
    print(i)

for i in range(3,51,3):
    print(i)

#18
# multiplication table
# num = int(input("enter a number:"))
# for i in range(1,11):
#     print(f"{num}x{i}={num}*{i}")

#19
# sum of number from 1 to 100
# total_sum = 0
# for i in range(1,101):
#     total_sum += i
#     print(total_sum)

#20
# num = int(input("enter a number:"))
# factorial = 1
# for i in range(1,num +1):
#     factorial = factorial *i
# print(f"factorial of {num} is:",factorial)

#21
# fruits = ["apple","orange","grape","pine apple","pappaya"]
# for fruit in fruits:
#     print(fruit)

#22
# numbers = [12,45,2,89,34,67]
# largest = numbers[0]
# for num in numbers:
#        if num > largest:
#         largest = num
# print("largest number is:",largest)

#23
# numbers= [12,45,2,89,12,7]
# dupli = set (numbers)  
# print(dupli)

#24
# student = {"student name": "keerthi","age": 24,"mark": 80}
# print(student)

#25
# fruits = ["apple","banana","orange","apple","grape","apple"]
# target = "apple"
# frequent = fruits.count(target)
# print(f"'{target}'{frequent}")



# numbers = [10,20,30,20,40,20,50]
# target = 20
# count= 0
# for num in numbers:
#     if num == target:
#         count +=1
#         print(f"'{target}'{count}")



#26  functions and oops
# def add_number(a,b):
#     return  a+b
# result = add_number(5,3)
# print(result)

# #27
# def check_prime(n):
#     if n <= 1:
#         return "not prime"
#     for i in range(2,n):
#         if n % i == 0:
#             return"not prime"
#     return"prime number"
# print(check_prime(2))

#28
class Student:
    def __init__(self,name,age,mark):
        self.name = name
        self.aage = age
        self.mark = mark

student1 = Student("keerthi",22,95)
print(student1.name)
print(student1.mark)

#29
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def withdraw(self,amount):
       if amount <= self.balance:
           self.balance-=amount
           return self.balance
       else:
           return "insufficient balance"
my_account= BankAccount(1000)
print(my_account.deposit(500))
print(my_account.withdraw(200))

        




 

