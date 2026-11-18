#**************************************#
#********** Function*******************#
#function to add 2 numbers
def display_sum(num1 , num2): # display is the function
    sum = num1 / num2         # input is num1 and num2

    print('the sum of ',num1 and num2,'is',sum)

# a function will have 
#1. function name
#2. input(s)
#3. body of the function (what the function actually does): mandatory
#4. output

# while we define input variables in the function definition, we are 
# creating new variables with scope within the function.

# call the function/ invoking the function
n1 = 99
n2 = 1

display_sum(n2, n1)  

display_sum(8,7)  
display_sum(2026,8)
display_sum(9.8,6.6)

def display_sum_custom():
    print('we will display the sum of the 2 number you enter')
    num1= float(input('enter first number:'))
    num2 = float(input('enter second number:'))
    sum = num1 +num2
    print('the sum of ',num1 and num2,'is',sum)
    
# display_sum_custom() # function call without input


def display_name_custom():
    print("we will display the name you enter")
    user = (input('enter name'))
    print("hi",user)
    print("good afternoon")
    print("how are you")

#display_name_custom()

# generating a multiplication table
num = 5
print('multiplication table of','num')
print('*************************')

for i in range (1,11):
    print(i,'x',num, '=',(i*num)) # 5 multiplication
      
#******************************************#

num = 8
print('multiplication table of','num')
print('*************************')

for i in range (1,11):
    print(i,'x',num, '=',(i*num)) # 8 multiplication

#function to display multiplication table of any number
def display_multiplication_table():
    print('we will display the multiplication table of the number you enter')
    # num= int(input("enter the number :"))
    print('**************************')
    print('multiplication table of',num)
    print('********************************')
    for i in range(1,11):
        # print(i,'x',num,'=',(i*num)) # eth num venm engilm multiplication table edkkan
        print(f"{i} x {num}= {i*num}")
# display_multiplication_table()  # invoking the function

#***********************************************#



def display_marks():
    print('we will display the sum of the 5 number you enter')

    marks=(50,88,66,23,44)
    
    sum = marks[0]+marks[1]+marks[2]+marks[3]+marks[4]
    print(sum)
    
#display_marks()

def display_marks():
    print('we will display the sum of the 5 number you enter')

    marks=(50,88,66,23,44)
    sum = marks[0]+marks[1]+marks[2]+marks[3]+marks[4]
    average = sum/len(marks)
    print(average)

    #we need to get score
    # 1.sum
    #2.average
    #3.largest
    #4.smallest

def calculate_sum(score_list):
    sum =0
    for i in range(len(score_list)):
        sum = sum+ score_list[i]

    print(f'total score = {sum}')
    return sum                      # output of the function

def calculate_avg(input_list):
    total= calculate_sum(input_list)
    count = len(input_list)
    average = total/count
    print(f'average score = {average}')
    return average

    
scores_list = [20,30,20,30,40]
total =calculate_avg(scores_list)         # whenever there is an output, we can assign it to a variable

print #************************************************************#
  # *********** optional argument*****************************

def calculate_exponent(num,exp=2): #here,exp is an output, default value here is'good day'
    print(num ** exp)
calculate_exponent(5)   
calculate_exponent(5,3)   

def create_wish(name,wish ='good day'):
    print(f'hi{name},{wish}')

create_wish("anjaly")
create_wish("anjaly",'good morning')   # positional arguments

create_wish(wish='Good afternoon',name='anjaly')

#*******************************************************#
#********python fundamentals question******************

#2
def calculate_result():
    python = 80
    maths = 70
    science = 60

    total = python + maths + science 
    print("total:",total)

    return total
calculate_result()

def average():
    python = 80
    maths = 70
    science = 60
    total=(python + maths + science)/3
    print("average:",total)
    return total

average()

def largest():
    python = 80
    maths = 70
    science = 60


    print("highest mark:", max(python , maths , science))
    print("lowest mark:",min(python , maths , science))





    #***********************************************#
    #***********************************************#

def divide(num,den):
        result = num/den
        print(f'the answer is {result}')


# divide(40,5)
# divide(1234,678)

# divide('a','b')

# exceptional handling
# we write specific criteria so that code flow is not interrupted.
# rewriting the function with exception block
# we write potential runtime errors making code inside 'try' block
# and the exception will be caght by the 'except' block.

def divide_new(num,den):
    try:
        result = num/den
        print(f'the answer is{result}')
    except:
        print('there is a problem')
        print('you reach the end of the function')
divide_new(40,5)
divide_new('a','b')
divide_new(3377,0) 
divide_new(55,5) 
# rewriting the function with exception block display the error message. 

def divide_new1(num,den):
    try:
        result = num/den
        print(f'the answer is{result}')
    except Exception as e:
        print(f'there is a problem: {e}')
        print('you reach the end of the function')
divide_new1(40,5)
divide_new1('a','b')
divide_new1(3377,0) 

#rewriting the function with exception block display appropriate
def divide_new2(num,den):
    try:
        result = num/den
        print(f'the answer is{result}')
    except TypeError:
        print('please make sure you are entering number')
    except ZeroDivisionError:
        print('please make sure to give a non zero value as denominator')
    except Exception as e:
        print(f'there is a problem : {e}')
        print('you reach the end of the function')
divide_new2(40,5)
divide_new2('a','b')
divide_new2(3377,0) 

