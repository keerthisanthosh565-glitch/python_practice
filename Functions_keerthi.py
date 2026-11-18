#1
def calculate_grade():
    print('we will display calculate_grade you enter')
    marks = int(input('enter you marks'))
    
    if(marks >= 90):
        print("A")
    elif(marks >=75):
        print("B")
    elif(marks >=60):
        print("C")
    elif(marks >=40):
        print("D")
    else:
        ("fail")


calculate_grade()

#2 
def calculator():
    num1 = int(input('enter a number:'))
    num2 = int(input('enter another number:'))
    operator = input('enter a number:')
    if(operator =='+'):
        calculation = num1 + num2
        return calculation
        
    elif(operator == '-'):
        calculation = num1 -num2
        return calculation    

    elif(operator =='*'):
        calculation = num1 * num2
        return calculation    

    elif(operator == '/'):
       calculation = num1 /num2
       return calculation 

    else:
        ('invaild symbol')
        return calculation
sum=calculator()
print(sum)

#3
def simple_interest():
    principal =int(input('enter number:'))
    rate = int(input('enter number:'))
    time = int(input('enter number:'))
    interest = principal*rate*time
    return interest
simple_int=simple_interest()
print(simple_int)

#4
def last_character():
    string_ = input('enter a string')
    lst_char = string_[-1]
    return lst_char
last_char=last_character()
print(last_char) 

#5
def calculate_bill():
    unit = int(input('enter electricity unit consumed'))
    if(unit <= 100):
        bill = 5 * unit
        return bill
    elif(unit<=200):
        bill = 500+ (unit-100)*7
        return bill
    else:
        bill=1200+(unit - 200)*10
        return bill
total_bill = calculate_bill()

print(total_bill)

#6
def count_even():
    # number_1 = int(input('enter number'))
    number_1=[20,30,40,35,65]
    for i in range(len(number_1)):
        if number_1[i]%2==0:
            print(number_1[i])
count_even()