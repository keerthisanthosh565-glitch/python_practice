#1
number = int(input('please enter a number:'))

if(number >=0):
    print ('the number entered is positive ')
else:
    print('the number entered is negative')

#2
age =int(input('please enter  age:'))
if  age >= 18:
    print ('the number entered is eligible to vote')
else:
    print('not eligible to vote')

#3
number = input('please enter a number:')
number =int (number)

if(number % 4 ==0):
    print('its an even number')
else:
    print('its an odd number')

#4
password = 'keerthi123'
user_password = input('please enter password:')
if user_password == password:
    print("access granted")
else:
    print("access denied")

#5
user1 = int(input("please enter number1 :"))
user2 = int(input("please enter number2 :"))
if  user1 > user2:
    print("user 1 is greater")
elif(user2 > user1):
    print("user 2 is greater")
else:
  print("both are equal")

#6
marks = int(input("please enter marks"))
if marks < 0 or marks >100:
    print("invaild marks")
elif(marks >= 90):
    print("grade A")
elif( marks>= 80):
    print("grade B")
elif(marks >= 70):
    print("grade C")
elif(marks >= 60):
    print("grade D")
elif(marks >= 50):
    print("grade E")
else:(marks < 50)
print("fail")

#7
num1 = int(input("please enter num1:"))
num2 = int(input("please enter num2:"))
num3 = int(input("please enter num3:"))
if (num1 >= num2  >= num3 ):
    print("num1 is larger")
elif(num2 >= num1 >= num3):
    print("num2 is larer")
else:(num3 >= num2 >= num1)
print("num3 is larger")

#8
colour = input("please enter traffic light colour:")
if (colour == "red"):
    print("stop")
elif(colour == "yellow"):
    print("get ready")
elif(colour == "green"):
    print("go")
else:
    print("invalid signal")

#9
unit = int(input("please enter unit"))
if(unit <= 100):
    print("total", 100*2)
elif(unit <= 200):
    print("total", 100 * 2 + (100 - unit) *3)
elif(unit <= 250):
    print("total", 100 * 2 + 100 * 3 +(100 -unit)*5)
else:
    print("total", 1000 + (unit - 300)*7)







    
