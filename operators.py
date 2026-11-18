#*******************************
#******* Arithemetic ***********
#*******************************

# binary operations : we need min of 2 operands.

num1 = 389
num2 =5

sum = num1 + num2        # addition
difference = num1 - num2 # subtraction
product = num1 * num2    # multiplication 
division = num1 / num2   # division
exponent = num1 ** num2  # exponent
remainder = num1 % num2  # modulus
floor = num1 // num2     # floor division 

print( num1, '+', num2, ' = ', sum)
print( num1, '-', num2, ' = ', difference)
print( num1, '*', num2, ' = ', product)
print( num1, '/', num2, ' = ', division)
print( num1, 'to the power', num2, ' = ', exponent)
print( 'remainder of', num1 , '%', num2, ' = ', remainder) 
print( num1, '//', num2, ' = ', floor)

#*****************************************
#******* Relational values ***************
#*****************************************

print(num1, '>' , num2 , num2 , num1 > num2)   # True
print(num1, '<' , num2 , num2 , num1 < num2)   # False
print(num1, '>=' , num2 , num2 , num1 >= num2) # True 
print(num1, '<=' , num2 , num2 , num1 <= num2) # False  
print(num1, '==' , num2 , num2 , num1 == num2) #False 
print(num1, '!=' , num2 , num2 , num1 != num2) # True

#****************************************************
#*********** Logical*********************************
#****************************************************

# And - A11 has to be in agreement.
# OR  - At least 1 must be in agreement
# not - opposite 

# operands are boolean

statement_1 = True
statement_2 = False
statement_3 = True
statement_4 = False

# AND
print(statement_1 and statement_2) # True and false= false
print(statement_1 and statement_3) # True and True = True
print(statement_2 and statement_4) # false and false = false

#OR
print(statement_1 or statement_2) # True and false= true
print(statement_1 or statement_3) # True and True = True
print(statement_2 or statement_4) # false and false = false

#NOT
print(not statement_1 ) #  not True = false
print(not statement_2 ) #  not false = True  


